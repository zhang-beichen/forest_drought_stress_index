#%%
import arcpy
import glob
import os

idir = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\stdSM\\"
sm_list = glob.glob(idir+"*.tif")
sm_list.sort()
sm_file = "R:\\UnitedStates\\ForDRI_project-NEW\Data\\stdSM\\SM200001.tif" #load reference file

arcpy.CheckOutExtension("Spatial")
out_dir = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\stdSM_Masked\\"
#out_rmpl = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\NDVI_resample\\"
#out_mask = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\NDVI\\NDVI_mask\\"
for f in sm_list:
    fname = os.path.basename(f)
    arcpy.env.snapRaster = sm_file
    #arcpy.env.mask = sm_file
    outExtractByMask = arcpy.sa.ExtractByMask(f, sm_file)
    outExtractByMask.save(out_dir+fname)
    print(fname)
# %%
