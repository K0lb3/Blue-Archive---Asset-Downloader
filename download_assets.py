import requests
import os
from AssetBatchConverter import extract_assets
import UnityPy

ROOT = os.path.dirname(os.path.realpath(__file__))
RAW = os.path.join(ROOT, "raw")
EXT = os.path.join(ROOT, "extracted")
VERSION = os.path.join(ROOT, "version.txt")

import UnityPy


def main():
    path = ROOT
    app_id = "com.nexon.bluearchive"

    print("Fetching version")
    if os.path.exists(VERSION):
        with open(VERSION, "rt") as f:
            version = f.read()
    else:
        print("no local version found")
        version = update_apk_version(app_id, path)
    print(version)

    print("Fetch latest resource version")
    try:
        check = version_check(app_id, build_version=version)
    except Exception as e:
        print("error during resource version request")
        print("updating apk settings")
        version = update_apk_version(app_id, path)
        check = version_check(app_id, build_version = version)

    print("Updating resources/assets")
    update_resources(check["patch"]["resource_path"])


def version_check(app_id: str, api_version: str="v1.1", build_version: str = "1.35.115378"):
    req = requests.post(
        f"https://api-pub.nexon.com/patch/{api_version}/version-check",
        json={
            "market_game_id": app_id,
            "language": "en",
            "advertising_id": "00000000-0000-0000-0000-000000000000",
            "market_code": "playstore",
            "country": "US",
            "sdk_version": "187",  # doesn't seem to matter
            "curr_build_version": build_version,
            "curr_build_number": int(build_version.rsplit(".", 1)[1]),
            "curr_patch_version": 0,
        },
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-A908N Build/LMY49I)",
            "Host": "api-pub.nexon.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        },
    )
    res = req.json()

    # latest_build_version = res["latest_build_version"]
    # latest_build_number = res["latest_build_number"]
    # if latest_build_version != build_version or latest_build_number != build_number:
    #    return version_check(api_version, latest_build_version, latest_build_number)
    return res


def update_resources(resource_path, lang="en"):
    # 1. get resource data
    req = requests.get(resource_path)
    res = req.json()

    # 2. update resources
    resource_main_url = resource_path.rsplit("/", 1)[0]
    for resource in res["resources"]:
        # {
        # "group": "group2",
        # "resource_path": "JA/group2/e392fcd3de13100b67589ef873b1f6d4.bundle",
        # "resource_size": 25206,
        # "resource_hash": "42092be2cf4d14381107205e40ab08b1"
        # },
        update_resource(resource_main_url, resource)


def update_resource(resource_main_url, resource):
    url = f"{resource_main_url}/{resource['resource_path']}"
    if url.endswith(".bundle"):
        raw_path = os.path.join(RAW, *resource["resource_path"].split("/"))
    else:
        raw_path = os.path.join(EXT, *resource["resource_path"].split("/"))
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)

    if not (
        os.path.exists(raw_path)
        and os.path.getsize(raw_path) == resource["resource_size"]
    ):
        print(raw_path)
        data = requests.get(url).content
        with open(raw_path, "wb") as f:
            f.write(data)
        
        # Unity BundleFile
        if url.endswith(".bundle"):
            extract_assets(data)
            # extract with UnityPy


def update_apk_version(apk_id, path):
    print("downloading latest apk from QooApp")
    apk_data = download_QooApp_apk(apk_id)
    with open(os.path.join(path, "current.apk"), "wb") as f:
        f.write(apk_data)
    print("extracing app_version and api_version")
    version = extract_apk_version(apk_data)
    with open(VERSION, "wt") as f:
        f.write(version)

    return version


def extract_apk_version(apk_data):
    from zipfile import ZipFile
    import io
    import re

    with io.BytesIO(apk_data) as stream:
        with ZipFile(stream) as zip:
            # devs are dumb shit and keep moving the app version around
            with zip.open("assets/bin/Data/globalgamemanagers", "r") as f:
                env = UnityPy.load(f)
                for obj in env.objects:
                    if obj.type.name == "PlayerSettings":
                        build_version = re.search(
                            b"\d+?\.\d+?\.\d+", obj.get_raw_data()
                        )[0].decode()
                        return build_version
            # smali\com\nexon\pub\bar\q.smali has the v1.1 for Nexus


def download_QooApp_apk(apk):
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode

    query = urlencode(
        {
            "supported_abis": "x86,armeabi-v7a,armeabi",
            "sdk_version": "22",
        }
    )
    res = urlopen(
        Request(
            url=f"https://api.qoo-app.com/v6/apps/{apk}/download?{query}",
            headers={
                "accept-encoding": "gzip",
                "user-agent": "QooApp 8.1.7",
                "device-id": "80e65e35094bedcc",
            },
            method="GET",
        )
    )
    data = urlopen(res.url).read()
    return data


if __name__ == "__main__":
    main()
