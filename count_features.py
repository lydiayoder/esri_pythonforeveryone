
import arcpy
arcpy.env.workspace = "C:/Courses/PythonStart"
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list: 
    count = arcpy.management.GetCount(fc)
    print(count)

