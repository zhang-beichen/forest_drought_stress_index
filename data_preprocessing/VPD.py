import arcpy
import glob
import os

idir = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\stdVPD\\"
NDVI_list = glob.glob(idir+"*.tif")
NDVI_list.sort()
ndvi_file = "R:\\UnitedStates\\ForDRI_project-NEW\Data\\VPD_PRISM\\vpd200001.tif" #load reference file
t_prj = arcpy.Describe(ndvi_file).spatialReference #acquire target spatial reference
s_prj = arcpy.Describe(NDVI_list[0]).spatialReference #acquire souce spatial reference
ndvi_raster = arcpy.sa.Raster(ndvi_file) # read in the NDVI file as raster
extent = ndvi_raster.extent #acquire extend of the raster
cellsize =  arcpy.GetRasterProperties_management(ndvi_file, "CELLSIZEX") #acquire the cell size

#out_prj = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\NDVI_prj\\"
out_rmpl = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\stdVPD_resampled\\"
#out_mask = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\NDVI_mask\\"
for f in NDVI_list:
    fname = os.path.basename(f)
    arcpy.env.snapRaster = ndvi_file
    arcpy.env.mask = ndvi_file
    #arcpy.ProjectRaster_management(f, out_prj+fname, t_prj, "NEAREST", cellsize,"#" , "#", s_prj, "#")
    arcpy.Resample_management(f,out_rmpl+fname, cellsize, "CUBIC")
    print(fname)
