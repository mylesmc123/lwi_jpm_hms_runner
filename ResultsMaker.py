from pydsstools.heclib.dss import HecDss
from pydsstools.core import TimeSeriesContainer
import pandas as pd
import numpy as np
import glob
import plotly
from plotly.graph_objs import Scatter, Layout
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import json


# gageList = ['Amite', 'Maurepas', 'Tangipahoa', 'Tickfaw']

# gageList = [
#     'J_UpperAmite','J_Sandy_AmiteDS','J_at_ComiteDr','J_Amite_Comite',
#     'J_UpperTickfallOut','J_TwelveMiCrkOut','J_TickfallHoldenOutlet','J_UpperNatalOutlet',
#     'J_LittleTangOutlet','J_ChapOutlet'
#     ] 


with open("gage.json", "r") as read_file:
    gages = json.load(read_file)

parameter = 'Flow'
units = 'cfs'

eventList = ['2004_Matthew', '2005_Rita', '2012_Isaac']
basinList = ['25P', '50P', '75P']

#for testing
# basinList = ['ACT']
# eventList = ['2004_Matthew']       

for event in eventList:
    for basin in basinList:
        n_columns = 1
        n = len(gages['gages'].keys())
        i=0
        
        # Setup plotly figure
        # fig = make_subplots(  
        #     rows=n, 
        #     cols=n_columns, 
        #     # vertical_spacing=3,
        #     # padding = 
        #     # vertical_spacing=(1 / (n - 1)),
        #     subplot_titles=gageList
        # )

        # For each dss file, get precip-inc at a location
        dss_dir = fr"Z:\LWI\JPM_3bins_dss_output\{event}\{basin}"
        dss_files = glob.glob(dss_dir+"//*.dss")
        dss_files = sorted(dss_files)

        for i, gage in enumerate(gages['gages'].keys()):
        
            # concatenate dataframes for each sim to a single dataframe that will be output to a csv file
            df_gage = pd.DataFrame()
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
                    
                    # concatenate dataframes for each sim to a single dataframe that will be output to a csv file
                    df_gage = pd.concat([df_gage,df])
            

                    # fig.append_trace(
                    #     go.Scatter(
                    #         x=df.Times, 
                    #         y=df.Values,
                    #         name = sim,
                    #     ), 
                    #     row=i+1,
                    #     # row = 1, 
                    #     col=1
                    # )

                    
                
                fid.close()
            
            # concatenate dataframes for each sim to a single dataframe that will be output to a csv file
            # CSV Output Format: Ex Q_Matthew_PARA_001_500_G01 --> Parameter_PARA_AntecedentBasin_Sim#_G#
            g = gages['gages'][gage]['g_name']
            df_gage.to_csv(f'ResultsMaker_output/Q_{event}_PARA_{basin}_{g}.csv')



        # fig.update_layout(
        #             height=n*10000, 
        #             width=2300,
        #             showlegend=False, 
        #             title_text=f"JPM Parametric Rainfall Simulations. {event} - {parameter} ({units})",
        #             template= "plotly_dark",
        #             hoverlabel=dict(
        #                 font=dict(
        #                     family='sans-serif', size=22
        #                 ),
        #                 namelength= -1
        #             )
        #         )
        # fig.update_yaxes(automargin=True)
        # fig.write_html(f"{event} {basin} Results.html")