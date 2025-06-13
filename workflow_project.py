#Author: Lydia Yoder
#Date: 6/13/2025
#Purpose: This script reads all the feature classes in a
#geodatabase and copies them to a new feature dataset in
#a new geodatabase. Feature classes not already in the
#target coordinate system are projected. 

#Import libraries
import arcpy
import os

#Variables for paths, outputs, workspaces
mypath = "C:/Courses/PythonWorkflow"
gdb = "Transportation.gdb"
new_gdb = "Metro_Transport.gdb"
fds = "Metro_Network"
arcpy.env.workspace = os.path.join(mypath, gdb)
arcpy.env.overwriteOutput = True

#Create a new geodatabase
new_gdb_path = arcpy.CreateFileGDB_management(mypath, new_gdb)
print(f"The geodatabase {new_gdb} has been created.")

#Create a new feature dataset
arcpy.CreateFeatureDataset_management(new_gdb_path, fds, 2248)
print(f"The feature dataset {fds} has been created.")

#Copy over feature classes and project unprojected feature classes
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    desc = arcpy.da.Describe(fc)
    sr = desc["spatialReference"]
    new_fc = os.path.join(mypath, new_gdb, fds, fc)
    if sr.factoryCode == 2248: #WKID of target coordinate system
        arcpy.CopyFeatures_management(fc, new_fc)
        print(f"The feature class {fc} has been copied.")
    else:
        arcpy.Project_management(fc, new_fc, 2248)
        print(f"The feature class {fc} has been projected.")


