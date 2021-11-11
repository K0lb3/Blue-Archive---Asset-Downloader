from lib.TableService import TableZipFile
import os

from download_assets import EXT

TABLE_FP = os.path.join(EXT, "Preload", "TableBundles")
for table_file in os.listdir(TABLE_FP):
    if not table_file.endswith(".zip"):
        pass

    print("==", table_file, "==")

    # create dir for table
    table_dir_fp = os.path.join(TABLE_FP, table_file[:-4])
    os.makedirs(table_dir_fp)
    # dump files from zip to dir
    tz = TableZipFile(os.path.join(TABLE_FP, table_file))
    for name in tz.namelist():
        print("", name)
        data = tz.open(name).read()
        fp = os.path.join(table_dir_fp, name)
        with open(fp, "wb") as f:
            f.write(data)
