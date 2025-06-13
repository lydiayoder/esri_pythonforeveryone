import arcpy
mypath = "C:/Courses/PythonDesc/DC.gdb/Transportation"
arcpy.env.workspace = mypath
files = arcpy.ListDatasets()
print(files)












