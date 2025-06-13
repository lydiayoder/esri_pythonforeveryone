import arcpy
mypath = "C:/Courses/PythonDesc/DC.gdb/Transportation"
arcpy.env.workspace = mypath

#Describe a dataset
desc = arcpy.da.Describe("Traffic")
print(f'baseName: {desc["baseName"]}')
if desc["extension"] !="":
    print(f'extension: {desc["extension"]}')
print(f'dataType: {desc["dataType"]}')
if "shapeType" in desc:
    print(f'shapeType: {desc["shapeType"]}')

##for k, v in desc.items():
##    print(f'{k}: {v}')









