import numpy as np
import glob, os, sys
import rasterio
import pandas as pd
import gdal
import time
from sklearn.decomposition import PCA

# function to calcualte the eigenvectors
# this uses pandas dataframe of all the values for a given month 
# for all variables 
def CDIwt(data):
    #corr_mat = data.corr()
    #corr_mat = corr_mat.fillna(0)
    #corr_mat = np.array(corr_mat)
    data[data == np.inf] = np.nan
    data = data.fillna(0)
    pca = PCA(n_components=1)
    pca.fit(data)
    explained_var_ratio = pca.explained_variance_ratio_
    #explained_var = pca.explained_variance_
    components = pca.components_
    #eig_val, eig_vec = np.linalg.eig(corr_mat)
    #return eig_vec[:,0]**2, eig_val
    return components, explained_var_ratio


# function to read raster data
'''def read_file(f):
    with rasterio.open(f) as src:
        return(src.read(1))'''
    
def read_file(f):
    ds = gdal.Open(f)
    Array = ds.ReadAsArray()
    return Array

#-------------------------------------

wdir = '/work/tadesse/beichen/Work/ForestDri/NEW_DATA_2022'

#odir = '/work/tadesse/beichen/Work/ForestDri/eigenvalues_2022/'

# read mask files
mask_1 = np.array(read_file(wdir+'/NDVI/NDVI_200301.tif'))
mask_2 = np.array(read_file(wdir+'/VPD/VPD_200301.tif'))
mask_3 = np.array(read_file(wdir+'/SM/SM_200301.tif'))
mask_4 = np.array(read_file(wdir+'/GWS/GWS_200301.tif'))
mask_5 = np.array(read_file(wdir+'/SPI09/SPI09_200301.tif'))
mask_6 = np.array(read_file(wdir+'/SPEI12/SPEI12_200301.tif'))
mask_7 = np.array(read_file(wdir+'/EDDI12/EDDI200301.tif'))

mask_5[mask_5==-1] = np.nan
mask_6[mask_6==-1] = np.nan


for week in range(1,53):
    start = time.time()
    if week < 10: wk = '0'+str(week)
    if week > 9: wk = str(week)
    print('Week: ',wk)

    feddi = glob.glob(wdir+'/EDDI12/'+'*%s.tif'%wk)
    feddi.sort()
    fgws = glob.glob(wdir+'/GWS/'+'*%s.tif'%wk)
    fgws.sort()
    fndvi = glob.glob(wdir+'/NDVI/'+'*%s.tif'%wk)
    fndvi.sort() 
    fspei12 = glob.glob(wdir+'/SPEI12/'+'*%s.tif'%wk)
    fspei12.sort()
    fspei24 = glob.glob(wdir+'/SPEI24/'+'*%s.tif'%wk)
    fspei24.sort()
    fspei60 = glob.glob(wdir+'/SPEI60/'+'*%s.tif'%wk)
    fspei60.sort()
    fspi09 = glob.glob(wdir+'/SPI09/'+'*%s.tif'%wk)
    fspi09.sort()
    fspi12 = glob.glob(wdir+'/SPI12/'+'*%s.tif'%wk)
    fspi12.sort()
    fspi24 = glob.glob(wdir+'/SPI24/'+'*%s.tif'%wk)
    fspi24.sort()
    fspi60 = glob.glob(wdir+'/SPI60/'+'*%s.tif'%wk)
    fspi60.sort()
    fsm = glob.glob(wdir+'/SM/'+'*%s.tif'%wk)
    fsm.sort()
    fvpd = glob.glob(wdir+'/VPD/'+'*%s.tif'%wk)
    fvpd.sort()
    
    eddi_ar =np.array([read_file(x) for x in feddi])
    gws_ar =np.array([read_file(x) for x in fgws])
    ndvi_ar =np.array([read_file(x) for x in fndvi])    
    spei12_ar =np.array([read_file(x) for x in fspei12])
    spei24_ar =np.array([read_file(x) for x in fspei24])
    spei60_ar =np.array([read_file(x) for x in fspei60])
    spi09_ar =np.array([read_file(x) for x in fspi09])
    spi12_ar =np.array([read_file(x) for x in fspi12])
    spi24_ar =np.array([read_file(x) for x in fspi24])
    spi60_ar =np.array([read_file(x) for x in fspi60])
    sm_ar =np.array([read_file(x) for x in fsm])
    vpd_ar =np.array([read_file(x) for x in fvpd])
    
    spei12_ar[spei12_ar==-1] = np.nan
    spei24_ar[spei24_ar==-1] = np.nan
    spei60_ar[spei60_ar==-1] = np.nan
    
    spi09_ar[spi09_ar==-1] = np.nan
    spi12_ar[spi12_ar==-1] = np.nan
    spi24_ar[spi24_ar==-1] = np.nan
    spi60_ar[spi60_ar==-1] = np.nan
    
    out_eddi = np.empty((208,464))
    out_eddi[:] = np.nan

    out_gws = np.empty((208,464))
    out_gws[:] = np.nan

    out_ndvi = np.empty((208,464))
    out_ndvi[:] = np.nan

    out_spei12 = np.empty((208,464))
    out_spei12[:] = np.nan
    
    out_spei24 = np.empty((208,464))
    out_spei24[:] = np.nan
    
    out_spei60 = np.empty((208,464))
    out_spei60[:] = np.nan
    
    out_spi09 = np.empty((208,464))
    out_spi09[:] = np.nan
    
    out_spi12 = np.empty((208,464))
    out_spi12[:] = np.nan
    
    out_spi24 = np.empty((208,464))
    out_spi24[:] = np.nan
    
    out_spi60 = np.empty((208,464))
    out_spi60[:] = np.nan
    
    out_sm = np.empty((208,464))
    out_sm[:] = np.nan
    
    out_vpd = np.empty((208,464))
    out_vpd[:] = np.nan
    
    eig_val_arr = np.array([])
    var_ratio_arr = np.array([])
    
    for i in range(0,208):
        for j in range(0,464):
            mask = mask_1[i,j]*mask_2[i,j]*mask_3[i,j]*mask_4[i,j]*mask_5[i,j]*mask_6[i,j]*mask_7[i,j] #identify nan
            if not np.isnan(mask):
                print('(%d,%d) is under processing.'%(i,j))
                #print(i,j,mask[i,j], np.shape(eddi_ar), out_eddi[i,j])
                eddi = np.array(eddi_ar[:,i,j])
                gws = np.array(gws_ar[:,i,j])
                ndvi = np.array(ndvi_ar[:,i,j])
                spei12 = np.array(spei12_ar[:,i,j])
                spei24 = np.array(spei24_ar[:,i,j])
                spei60 = np.array(spei60_ar[:,i,j])
                spi09 = np.array(spi09_ar[:,i,j])
                spi12 = np.array(spi12_ar[:,i,j])
                spi24 = np.array(spi24_ar[:,i,j])
                spi60 = np.array(spi60_ar[:,i,j])
                sm = np.array(sm_ar[:,i,j])
                vpd = np.array(vpd_ar[:,i,j])
                
                
                #print(sld)
                df = pd.DataFrame({'eddi':eddi})
                df2 = pd.DataFrame({'gws':gws})
                df3 = pd.DataFrame({'ndvi':ndvi})
                df4 = pd.DataFrame({'spei12':spei12})
                df5 = pd.DataFrame({'spei24':spei24})
                df6 = pd.DataFrame({'spei60':spei60})
                df7 = pd.DataFrame({'spi09':spi09})
                df8 = pd.DataFrame({'spi12':spi12})
                df9 = pd.DataFrame({'spi24':spi24})
                df10 = pd.DataFrame({'spi60':spi60})
                df11 = pd.DataFrame({'sm':sm})
                df12 = pd.DataFrame({'vpd':vpd})

                df = pd.concat([df,df2], ignore_index=True, axis=1)
                df = pd.concat([df,df3], ignore_index=True, axis=1)
                df = pd.concat([df,df4], ignore_index=True, axis=1)
                df = pd.concat([df,df5], ignore_index=True, axis=1)
                df = pd.concat([df,df6], ignore_index=True, axis=1)
                df = pd.concat([df,df7], ignore_index=True, axis=1)
                df = pd.concat([df,df8], ignore_index=True, axis=1)
                df = pd.concat([df,df9], ignore_index=True, axis=1)
                df = pd.concat([df,df10], ignore_index=True, axis=1)
                df = pd.concat([df,df11], ignore_index=True, axis=1)
                df = pd.concat([df,df12], ignore_index=True, axis=1)
 
                component, explained_var_ratio = CDIwt(df)
    
                #eig_val_arr = np.append(eig_val_arr,explained_var.reshape(1,12))
                var_ratio_arr = np.append(var_ratio_arr,explained_var_ratio)
                
                out_eddi[i,j] = component[0,0]**2
                out_gws[i,j] = component[0,1]**2
                out_ndvi[i,j] = component[0,2]**2
                out_spei12[i,j] = component[0,3]**2
                out_spei24[i,j] = component[0,4]**2
                out_spei60[i,j] = component[0,5]**2
                out_spi09[i,j] = component[0,6]**2
                out_spi12[i,j] = component[0,7]**2
                out_spi24[i,j] = component[0,8]**2
                out_spi60[i,j] = component[0,9]**2
                out_sm[i,j] = component[0,10]**2
                out_vpd[i,j] = component[0,11]**2
               
                # set timeseries array to nan
                eddi[:] = np.nan
                gws[:] = np.nan
                ndvi[:] = np.nan
                spei60[:] = np.nan
                spei12[:] = np.nan
                spei24[:] = np.nan
                spi09[:] = np.nan
                spi12[:] = np.nan
                spi24[:] = np.nan
                spi60[:] = np.nan
                sm[:] = np.nan
                vpd[:] = np.nan
                
                del component, explained_var_ratio
                
    #np.savetxt(odir+wk+".csv", eig_val_arr, delimiter=",")
    np.savetxt(wdir+'/Eigenvalues/ratio_'+wk+".csv", var_ratio_arr, delimiter=",")
    
    with rasterio.open(feddi[0]) as src:
        meta = src.meta
        meta.update(dtype=rasterio.float32)
    
    outfeddi = os.path.join(wdir+'/weights/EDDI12/EDDI_'+wk+'.tif')
    with rasterio.open(outfeddi, 'w', **meta) as dst:
        dst.write(out_eddi.astype(rasterio.float32), 1)
    #np.save(outfeddi,out_eddi, allow_pickle=True)
    print('EDDI_%s is done!'%wk)

    outfgws = os.path.join(wdir+'/weights/GWS/GWS_'+wk+'.tif')
    with rasterio.open(outfgws, 'w', **meta) as dst:
        dst.write(out_gws.astype(rasterio.float32), 1)
    #np.save(outfgws,out_gws, allow_pickle=True)
    print('GWS_%s is done!'%wk)

    outfndvi = os.path.join(wdir+'/weights/NDVI/NDVI_'+wk+'.tif')
    with rasterio.open(outfndvi, 'w', **meta) as dst:
        dst.write(out_ndvi.astype(rasterio.float32), 1)
    #np.save(outfndvi,out_ndvi, allow_pickle=True)
    print('NDVI_%s is done!'%wk)

    outfspei12 = os.path.join(wdir+'/weights/SPEI12/SPEI12_'+wk+'.tif')
    with rasterio.open(outfspei12, 'w', **meta) as dst:
        dst.write(out_spei12.astype(rasterio.float32), 1)
    #np.save(outfspei12,out_spei12, allow_pickle=True)
    print('SPEI12_%s is done!'%wk)
        
    outfspei24 = os.path.join(wdir+'/weights/SPEI24/SPEI24_'+wk+'.tif')
    with rasterio.open(outfspei24, 'w', **meta) as dst:
        dst.write(out_spei24.astype(rasterio.float32), 1)
    #np.save(outfspei24,out_spei24, allow_pickle=True)
    print('SPEI24_%s is done!'%wk)
    
    outfspei60 = os.path.join(wdir+'/weights/SPEI60/SPEI60_'+wk+'.tif')
    with rasterio.open(outfspei60, 'w', **meta) as dst:
        dst.write(out_spei60.astype(rasterio.float32), 1)
    #np.save(outfspei60,out_spei60, allow_pickle=True)
    print('SPEI60_%s is done!'%wk)
    
    outfspi09 = os.path.join(wdir+'/weights/SPI09/SPI09_'+wk+'.tif')
    with rasterio.open(outfspi09, 'w', **meta) as dst:
        dst.write(out_spi09.astype(rasterio.float32), 1)
    #np.save(outfspi09,out_spi09, allow_pickle=True)
    print('SPI09_%s is done!'%wk)
    
    outfspi12 = os.path.join(wdir+'/weights/SPI12/SPI12_'+wk+'.tif')
    with rasterio.open(outfspi12, 'w', **meta) as dst:
        dst.write(out_spi12.astype(rasterio.float32), 1)
    #np.save(outfspi12,out_spi12, allow_pickle=True)
    print('SPI12_%s is done!'%wk)
    
    outfspi24 = os.path.join(wdir+'/weights/SPI24/SPI24_'+wk+'.tif')
    with rasterio.open(outfspi24, 'w', **meta) as dst:
        dst.write(out_spi24.astype(rasterio.float32), 1)
    #np.save(outfspi24,out_spi24, allow_pickle=True)
    print('SPI24_%s is done!'%wk)
    
    outfspi60 = os.path.join(wdir+'/weights/SPI60/SPI60_'+wk+'.tif')
    with rasterio.open(outfspi60, 'w', **meta) as dst:
        dst.write(out_spi60.astype(rasterio.float32), 1)
    #np.save(outfspi60,out_spi60, allow_pickle=True)
    print('SPI60_%s is done!'%wk)
    
    outfsm = os.path.join(wdir+'/weights/SM/SM_'+wk+'.tif')
    with rasterio.open(outfsm, 'w', **meta) as dst:
        dst.write(out_sm.astype(rasterio.float32), 1)
    #np.save(outfsm,out_sm, allow_pickle=True)
    print('SM_%s is done!'%wk)
    
    outfvpd = os.path.join(wdir+'/weights/VPD/VPD_'+wk+'.tif')
    with rasterio.open(outfvpd, 'w', **meta) as dst:
        dst.write(out_vpd.astype(rasterio.float32), 1)
    #np.save(outfvpd,out_vpd, allow_pickle=True)
    print('VPD_%s is done!'%wk)
    
    end = time.time()
    print('Week %s is done. It takes %.2f minutes.'%(wk,(end-start)/60))
print("All weights and explained ratio are completed.")