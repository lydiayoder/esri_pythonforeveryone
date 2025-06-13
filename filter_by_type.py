import arcpy
mypath = "C:/Courses/PythonDesc/DC.gdb"
arcpy.env.workspace = mypath
##files = arcpy.ListFeatureClasses()
##count_point = 0
##count_line = 0
##count_poly = 0
##for file in files:
##    desc = arcpy.da.Describe(file)
##    if desc["shapeType"] == "Point":
##        count_point += 1
##    if desc["shapeType"] == "Polygon":
##        count_poly += 1
##    if desc["shapeType"] == "Polyline":
##        count_line += 1
count_point = len(arcpy.ListFeatureClasses(feature_type = "POINT"))
count_line = len(arcpy.ListFeatureClasses(feature_type = "LINE"))
count_poly = len(arcpy.ListFeatureClasses(feature_type = "POLYGON"))
print(f'Count of Point feature classes: {count_point}')
print(f'Count of Polygon feature classes: {count_poly}')
print(f'Count of Polyline feature classes: {count_line}')











