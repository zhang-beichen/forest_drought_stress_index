#%%
import arcpy
import glob
import os

#idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\'
idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_9_mn\\'
odir = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spi12_resample\\"

#SPI12
dir_spi = idir+"spi12_mn_2003_2020\\"
spi_list = glob.glob(dir_spi+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\SPI12n\\SPI12198001.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+1
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPI12_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
# %%
import arcpy
import glob
import os

idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\'
odir = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spi24_resample\\"

#SPI24
dir_spi = idir+"spi24_mn_2003_2020\\"
spi_list = glob.glob(dir_spi+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\SPI24n\\SPI24198001.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+1
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPI24_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
# %%
import arcpy
import glob
import os

odir = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spi60_resample\\"

#SPI60
dir_spi = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spi60_mn_2003_2020\\"
spi_list = glob.glob(dir_spi+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\SPI24n\\SPI24198001.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+1
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPI60_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
#%%
import arcpy
import glob
import os

odir = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spei12_resample\\"

#SPEI12
dir_spi = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spei12_mn_2003_2020\\"
spi_list = glob.glob(dir_spi+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\SPEI12n\\SPEI12198001.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+1
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPEI12_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
# %%
import arcpy
import glob
import os

odir = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spei24_resample\\"

#SPEI24
dir_spi = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spei24_mn_2003_2020\\"
spi_list = glob.glob(dir_spi+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\SPEI24n\\SPEI24198001.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+1
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPEI24_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
#%%
import arcpy
import glob
import os

odir = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spei60_resample\\"

#SPEI60
dir_spi = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\ForDRI-data_Chris\\spei60_mn_2003_2020\\"
spi_list = glob.glob(dir_spi+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\Data\\SPEI24n\\SPEI24198001.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+1
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPEI60_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
    
    
    
# %%
import arcpy
from arcpy.sa import *
import glob
import os

arcpy.CheckOutExtension("Spatial")

#SPI09
idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_9_mn\\'
odir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_9_mn_resampled\\'

spi_list = glob.glob(idir+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\INPUT_NEW_DATA_2022\\SPI09\\SPI09_200301.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+14 # from 4 April
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPI09_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    f = Divide(f, 100.0) # remove the scalar
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)

# %%
import arcpy
from arcpy.sa import *
import glob
import os

arcpy.CheckOutExtension("Spatial")

#SPI12
idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_12_mn\\'
odir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_12_mn_resampled\\'

spi_list = glob.glob(idir+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\INPUT_NEW_DATA_2022\\SPI12\\SPI12_200301.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+14 # from 4 April
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPI12_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    f = Divide(f, 100.0) # remove the scalar
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
    
# %%
import arcpy
from arcpy.sa import *
import glob
import os

arcpy.CheckOutExtension("Spatial")

#SPI24
idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_24_mn\\'
odir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_24_mn_resampled\\'

spi_list = glob.glob(idir+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\INPUT_NEW_DATA_2022\\SPI24\\SPI24_200301.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+14 # from 4 April
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPI24_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    f = Divide(f, 100.0) # remove the scalar
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
    
# %%
import arcpy
from arcpy.sa import *
import glob
import os

arcpy.CheckOutExtension("Spatial")

#SPI60
idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_60_mn\\'
odir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPI\\spi_60_mn_resampled\\'

spi_list = glob.glob(idir+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\INPUT_NEW_DATA_2022\\SPI60\\SPI60_200301.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+14 # from 4 April
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPI60_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    f = Divide(f, 100.0) # remove the scalar
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)

# %%
import arcpy
from arcpy.sa import *
import glob
import os

arcpy.CheckOutExtension("Spatial")

#SPEI12
idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPEI\\spei_12_mn\\'
odir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPEI\\spei_12_mn_resampled\\'

spi_list = glob.glob(idir+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\INPUT_NEW_DATA_2022\\SPEI12\\SPEI12_200301.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+14 # from 4 April
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPEI12_'+year+str_month+'.tif' #output file

    arcpy.env.snapRaster = ref_file
    f = Divide(f, 100.0) # remove the scalar
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
    
# %%
import arcpy
from arcpy.sa import *
import glob
import os

#SPEI24
idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPEI\\spei_24_mn\\'
odir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPEI\\spei_24_mn_resampled\\'

spi_list = glob.glob(idir+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\INPUT_NEW_DATA_2022\\SPEI24\\SPEI24_200301.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

arcpy.CheckOutExtension("Spatial")

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+14 # from 4 April
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPEI24_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    
    f = Divide(f, 100.0) # remove the scalar
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
    
# %%
import arcpy
from arcpy.sa import *
import glob
import os

arcpy.CheckOutExtension("Spatial")

#SPEI60
idir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPEI\\spei_60_mn\\'
odir = 'R:\\UnitedStates\\ForDRI_project-NEW\\Case_Study_2022_Growing_Season\SPEI\\spei_60_mn_resampled\\'

spi_list = glob.glob(idir+"*.tif")
spi_list.sort()

ref_file = "R:\\UnitedStates\\ForDRI_project-NEW\\New_Model_2022\\INPUT_NEW_DATA_2022\\SPEI60\\SPEI60_200301.tif"
cellsize =  arcpy.GetRasterProperties_management(ref_file, "CELLSIZEX") #acquire the cell size

for idx, f in enumerate(spi_list):
    fname = os.path.basename(f).split("_")[3]
    year = fname[:4]
    month = idx%52+14 # from 4 April
    if month < 10:
        str_month = '0'+str(month)
    else:
        str_month = str(month)
    
    output = odir+'SPEI60_'+year+str_month+'.tif' #output file
    arcpy.env.snapRaster = ref_file
    f = Divide(f, 100.0) # remove the scalar
    arcpy.Resample_management(f, output, cellsize, "NEAREST")
    print(fname)
# %%
