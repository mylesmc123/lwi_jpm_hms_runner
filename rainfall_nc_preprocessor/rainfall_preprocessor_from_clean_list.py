import xarray as xr
import glob, os, tqdm
import pandas as pd

in_dir = r"V:\projects\p00542_cpra_2020_lwi_t10\00_collection\data\rainfall\download"
out_dir = r"V:\projects\p00542_cpra_2020_lwi_t10\00_collection\data\rainfall\time_fixed_nc"

df = pd.read_csv('cleanList.csv')

for f in tqdm.tqdm(df['0'].iloc[70:]):
    print(f)
    stormId = f.split("_")[3]
    ensembleId = f.split("_")[4].split(".")[0]
    destination = out_dir + '//' + f
    ds = xr.open_dataset(f'{in_dir}//storm_{stormId}//{f}')
    ds.time.attrs["units"] = "hours since 2050-01-05 23:30:00 GMT"
    ds.to_netcdf(destination)
    ds.close()