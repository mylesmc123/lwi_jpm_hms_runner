import glob
import os

# event = "Hurricane_Isaac"

basinList = ["25P", "50P","75P"]
precip_eventList = ["Hurricane_Isaac", "Hurricane_Rita", "TS_Matthew"]

for event in precip_eventList:
    for basin in basinList:
        apart = event.split("_")[-1]
        precip_dss_dir = fr'Z:\Amite\precipitation\JPM_Parametric\{event}'
        grid_fn = os.path.join(os.getcwd(),f'HMSFileMaker_output/{basin}/Amite_Final_HMS_Model.grid')
        run_fn = os.path.join(os.getcwd(),f'HMSFileMaker_output/{basin}/Amite_Final_HMS_Model.run')
        hms_fn = os.path.join(os.getcwd(),f'HMSFileMaker_output/{basin}/Amite_Final_HMS_Model.hms')

        # Get each sim
        dss_files = glob.glob(precip_dss_dir+"//*.dss")
        dss_files = sorted(dss_files)
        for dss_file in dss_files:
            sim = dss_file.split(".")[0].split("_")[-1]
            
            # Grid file append each sim.
            with open(grid_fn, 'a') as gridFile:
                gridFile.write(f"""
Grid: {event}_{basin}_JPM_{sim}
    Grid Type: Precipitation
    Last Modified Date: 27 September 2022
    Last Modified Time: 22:34:58
    Reference Height Units: Meters
    Reference Height: 10.0
    Data Source Type: External DSS
    Variant: Variant-1
        Last Variant Modified Date: 27 September 2022
        Last Variant Modified Time: 22:34:58
        Default Variant: Yes
        DSS File Name: {dss_file}
        DSS Pathname: /{apart}//PRECIPITATION///{sim}/
    End Variant: Variant-1
    Use Lookup Table: No
End:
    """)

            # create new met file for each sim. JPM_Sim###.met
            met_fn = os.path.join(os.getcwd(),f'HMSFileMaker_output/{basin}/{event}_{basin}_JPM_{sim}.met')
            with open(met_fn, "w") as metFile:
                metFile.write(f"""Meteorology: {event}_{basin}_JPM_{sim}
    Last Modified Date: 27 September 2022
    Last Modified Time: 20:54:09
    Version: 4.10
    Unit System: Metric
    Set Missing Data to Default: Yes
    Precipitation Method: Gridded Precipitation
    Air Temperature Method: None
    Atmospheric Pressure Method: None
    Dew Point Method: None
    Wind Speed Method: None
    Shortwave Radiation Method: None
    Longwave Radiation Method: None
    Snowmelt Method: None
    Evapotranspiration Method: No Evapotranspiration
End:

Precip Method Parameters: Gridded Precipitation
    Last Modified Date: 27 September 2022
    Last Modified Time: 20:54:19
    Precip Grid Name: {event}_{basin}_JPM_{sim}
End:
        """)

            # Run file append each sim
            with open(run_fn, 'a') as runFile:
                runFile.write(f"""
Run: {event}_{basin}_JPM_{sim}
    Default Description: Yes
    Log File: {event}_{basin}_JPM_{sim}.log
    DSS File: {event}_{basin}_JPM_{sim}.dss
    Is Save Spatial Results: Yes
    Spatial Results Write Interval: 60
    Last Modified Date: 27 September 2022
    Last Modified Time: 21:50:21
    Last Execution Date: 27 September 2022
    Last Execution Time: 22:35:01
    Basin: Consensus- Grid
    Precip: {event}_{basin}_JPM_{sim}
    Control: {event}
    Save State Type: None
    Time-Series Output: Save All
    Time Series Results Manager Start:
    Time Series Results Manager End:
End:
        """)

        # HMS file append each sim
            with open(hms_fn, 'a') as hmsFile:
                hmsFile.write(f"""
Precipitation: {event}_{basin}_JPM_{sim}
    Filename: {event}_{basin}_JPM_{sim}.met
    Description: 
    Last Modified Date: 27 September 2022
    Last Modified Time: 22:34:58
End:
    """)

