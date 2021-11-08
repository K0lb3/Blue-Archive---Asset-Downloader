from lib.TableService import TableZipFile
import os
from lib.TableEncryptionService import XOR

tz = TableZipFile(r"D:\Datamine\Blue Archive\extracted\Preload\TableBundles\Excel.zip")
os.makedirs("excel_raw", exist_ok=True)
for name in tz.namelist():
    fp = os.path.join("excel_raw", name)
    data = tz.open(name).read()
    xored = XOR(name, data)
    with open(fp, "wb") as f:
        f.write(data)