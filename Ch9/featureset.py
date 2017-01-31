import arcpy
from pprint import pprint

#create a feature set using a feature class
f_set = arcpy.FeatureSet(r"C:\PythonBook\Scripts\PacktDB.gdb\SanFrancisco\Bus_Stops")

bus_signage = {row[0]:row[1] for row in arcpy.da.SearchCursor(f_set,["NAME","BUS_SIGNAG"])}

pprint(bus_signage)
