from download_assets import ROOT, RAW, EXT
import AssetBatchConverter

AssetBatchConverter.DST= EXT


import os
for root, dirs, files in os.walk(RAW):
    for f in files:
        if not f.endswith(".bundle"):
            continue
        fp = os.path.join(root, f)
        AssetBatchConverter.extract_assets(fp)