from lib.TableService import TableZipFile
import os
import json
from lib.StringCipher import Decrypt
from lib.TableEncryptionService import CreateKey
from download_assets import EXT
from lib.XXHashService import CalculateHash

TABLE_FP = os.path.join(EXT, "Preload", "TableBundles")
for table_file in os.listdir(TABLE_FP):
    if not table_file.endswith(".zip"):
        continue

    print("==", table_file, "==")

    # create dir for table
    table_dir_fp = os.path.join(TABLE_FP, table_file[:-4])
    os.makedirs(table_dir_fp, exist_ok=True)
    # dump files from zip to dir
    tz = TableZipFile(os.path.join(TABLE_FP, table_file))
    for name in tz.namelist():
        print("", name)
        data = tz.open(name).read()
        
        if name.endswith(".json"):
            if name == "logiceffectdata.json":
                data = Decrypt(data, "LogicEffectData").encode("utf8")
            elif name == "newskilldata.json":
                data = Decrypt(data, "NewSkillData").encode("utf8")

        fp = os.path.join(table_dir_fp, name)
        with open(fp, "wb") as f:
            f.write(data)
