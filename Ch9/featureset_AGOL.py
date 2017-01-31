import arcpy

#ArcGIS Online Feature Service of SF Bus Stops
bus_stops_url = "http://services7.arcgis.com/LLWzNvydeNCpjeTo/arcgis/rest/services/BusStops/FeatureServer/0/query?where=OBJECTID>0&outFields=*&f=json"
#Create the feature set
bus_featureset = arcpy.FeatureSet()
#load the json data into the feature set
bus_featureset.load(bus_stops_url)
#Next we'll save the feature set data to a feature class in our geodatabase
bus_featureset.save(r"C:\PythonBook\Scripts\PacktDB.gdb\SanFrancisco\agol_bus2")
