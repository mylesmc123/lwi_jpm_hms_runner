from pydsstools.heclib.dss import HecDss
from pydsstools.core import TimeSeriesContainer
import pandas as pd
import numpy as np
import glob
import plotly
from plotly.graph_objs import Scatter, Layout
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# For each dss file, get precip-inc at a location
dss_dir = r"Z:\LWI\EJPM-OS-Param-Rainfall-Tests\hms_out_dss\2004_Matthew"
dss_files = glob.glob(dss_dir+"//*.dss")
dss_files = sorted(dss_files)

event = 'Hurricane Matthew (2004)'
gageList = ['Amite', 'Maurepas', 'Tangipahoa', 'Tickfaw']
parameter = 'PRECIP-INC'
units = 'mm'
n_columns = 1
n = len(gageList)
        
# Setup plotly trace
fig = make_subplots(  
    rows=n, 
    cols=n_columns, 
    vertical_spacing=.1,
    # vertical_spacing=(1 / (n - 1)),
    subplot_titles=gageList
)

for i, gage in enumerate(gageList):
    for dss_file in dss_files:
        
        sim = dss_file.split(".")[0].split("_")[-1]
        fid = HecDss.Open(fr"{dss_file}")
        pathname_pattern = f'//{gage}/{parameter}/*/1HOUR/*/'
        path_list = fid.getPathnameList(pathname_pattern,sort=1)
        subbasinList = []
        DSSpaths_List = []
        
        for path in path_list:
            
            pathSplit = path.split("/")
            subbasin = pathSplit[2]
            cPart = pathSplit[3]
            ePart = pathSplit[5]
            fPart = pathSplit[6]
            subbasinList.append(subbasin)
            
            # Remove d-part
            noDpartPath = f"//{subbasin}/{cPart}//{ePart}/{fPart}/"
            DSSpaths_List.append(noDpartPath)
        
        # sort the lists alphabetically, and remove dups
        subbasinList = sorted(list(set(subbasinList)))
        DSSpaths_List = sorted(list(set(DSSpaths_List)))
        
        n = len(DSSpaths_List)
        subPlotTitleList  = subbasinList

        for path in DSSpaths_List:
            
            ts = fid.read_ts(path)
            
            # setup dataframe of trace
            df = pd.DataFrame()
            df['Times'] = ts.pytimes
            df['Values'] = ts.values
            df['Missing'] = ts.nodata
            df.Values = np.where(df.Missing == True, np.NaN, df.Values)
            df['sim'] = sim
            
            

            fig.append_trace(
                go.Scatter(
                    x=df.Times, 
                    y=df.Values,
                    name = sim,
                ), 
                row=i+1,
                # row = 1, 
                col=1
            )

            
        
        fid.close()
    
    # fig.add_annotation(
    #             text=gage,
    #             xref="x domain", yref="y domain",
    #             x=0.9, y=0.9, showarrow=False,
    #             row=i+1,
    #             # row = 1, 
    #             col=1,
    #             font=dict(family='sans-serif', size=22)
    #         )

fig.update_layout(
            height=n*1800, 
            width=2300,
            showlegend=False, 
            title_text=f"JPM Parametric Rainfall Simulations. {event} - {parameter} ({units})",
            template= "plotly_dark",
            hoverlabel=dict(
                font=dict(
                    family='sans-serif', size=22
                ),
                namelength= -1
            )
        )

fig.write_html("Results.html")