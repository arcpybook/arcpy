import arcpy
from arcpy_token import return_token, submit_request
#make it possible to overwrite an existing feature class
arcpy.env.overwriteOutput = True
#assign the feature class we will be updating to the variable update
update = r"C:\PythonBook\Scripts\PacktDB.gdb\Chapter9Results\BusStops_Moved_Update"

user_file = open('username.txt', 'r')
username = user_file.readline().rstrip('\n')
pass_file = open('password.txt', 'r')
password = pass_file.readline().rstrip('\n')
service_url = "https://arcgis.com/sharing"

def update_featureclass_agol(base_URL, update_feature, count):
    n = 0
    template = r"C:\PythonBook\Scripts\PacktDB.gdb\SanFrancisco\Bus_Stops"
    FC = arcpy.CreateFeatureclass_management("in_memory", "FC", "POINT", template, "DISABLED", "DISABLED", "", "", "0", "0", "0")
    token = return_token(service_url, username, password)
    for x in range(count):
        where = "OBJECTID>"+str(n)
        query = "/query?where={}&returnGeometry=true&outSR=2227&outFields=*&f=json&token={}".format(where, token)

        fs_URL = base_URL + query
        fs = arcpy.FeatureSet()
        fs.load(fs_URL)
        arcpy.Append_management (fs, FC, "NO_TEST")

        n+=1000

        print n

    with arcpy.da.SearchCursor(FC, ['OID@', 'SHAPE@XY', "FACILITYID"]) as cursor:
        for row in cursor:
            objectid = row[0]
            pointx = row[1][0]
            pointy = row[1][1]
            fid = row[2]

            fid_sql ="FACILITYID = {0}".format(fid)
            with arcpy.da.UpdateCursor(update_feature, ['SHAPE@'], fid_sql) as cursor:
                for urow in cursor:
                    print "FACILITYID updated is ", fid
                    urow[0] = arcpy.Point(pointx, pointy)
                    cursor.updateRow(urow)

def main():
    update_featureclass_agol("https://services7.arcgis.com/LLWzNvydeNCpjeTo/arcgis/rest/services/BusStops/FeatureServer/0", update, 17)

if __name__ == '__main__':
    main()
