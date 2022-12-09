import xarray as xr
import glob, os, tqdm
import pandas as pd

in_dir = r"V:\projects\p00542_cpra_2020_lwi_t10\00_collection\data\rainfall\download"
f = glob.glob(fr"{in_dir}\**\*.nc", recursive=True)
out_dir = r"V:\projects\p00542_cpra_2020_lwi_t10\00_collection\data\rainfall\time_fixed_nc"

f.sort()
df = pd.DataFrame(f, columns =['f'])
df.to_csv('fileList2.csv')
for afile in tqdm.tqdm(f[67502:]):
    head, tail = os.path.split(afile)
    stormId = tail.split("_")[3]
    ensembleId = tail.split("_")[4].split(".")[0]
    destination = out_dir + '//' + tail
    ds = xr.open_dataset(afile)
    ds.time.attrs["units"] = "hours since 2050-01-05 23:30:00 GMT"
    ds.to_netcdf(destination)
    ds.close()