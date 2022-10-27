#%%
import arcpy
import glob
import os

idir = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\weekly_NDVI_2018_2020\\"
NDVI_list = glob.glob(idir+"*.tif")
NDVI_list.sort()
ndvi_file = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\NDVI_final\\eMODIS200001.tif" #load reference file
t_prj = arcpy.Describe(ndvi_file).spatialReference #acquire target spatial reference
s_prj = arcpy.Describe(NDVI_list[0]).spatialReference #acquire souce spatial reference
ndvi_raster = arcpy.sa.Raster(ndvi_file) # read in the NDVI file as raster
extent = ndvi_raster.extent #acquire extend of the raster
cellsize =  arcpy.GetRasterProperties_management(ndvi_file, "CELLSIZEX") #acquire the cell size

out_prj = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\NDVI_prj\\"
#out_rmpl = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\NDVI_resample\\"
#out_mask = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\NDVI_mask\\"
for f in NDVI_list:
    fname = os.path.basename(f)
    arcpy.env.snapRaster = ndvi_file
    arcpy.env.mask = ndvi_file
    arcpy.ProjectRaster_management(f, out_prj+fname, t_prj, "CUBIC", cellsize,"#" , "#", s_prj, "#")
    print(fname)
    


# %%
NDVI_list