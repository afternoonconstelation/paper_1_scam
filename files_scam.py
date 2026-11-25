# -*- coding: UTF-8 -*-
###################################################
#PYTHON CODE TO PLOT DIFFERENS

#MPAS DATA USING CARTOPY AND XARRAY.
###################################################
#PYTHON CODE TO PLOT DIFFERENS
#End=`date +%s.%N`
###################################################
# By: Jhonatan A. A Manco

###################################################
# Function to load the complete ncfiles  of regional MONAN run
from   scam  import data_own as down
from pathlib import Path


exp_name             = 'GOAIOP1_UW_FLX'
path_goaiop1_uw_flx  = './data/SCAM_GOAIOP1_UW_FLX.cam.h0i.2014-02-15-01800.nc'
goaiop1_uw_flx       = down.data_load_xr(path_goaiop1_uw_flx, exp_name, -4)

exp_name             = 'GOAIOP2_UW_FLX'
path_goaiop2_uw_flx  = './data/SCAM_GOAIOP2_UW_FLX.cam.h0i.2014-09-01-01800.nc'
goaiop2_uw_flx       = down.data_load_xr(path_goaiop2_uw_flx, exp_name, -4)

exp_name          = 'GOAIOP1_CLUBB_FLX'
path_goaiop1_clubb_flx  = './data/SCAM_GOAIOP1_FLX.cam.h0i.2014-02-15-01800.nc'
goaiop1_clubb_flx = down.data_load_xr(path_goaiop1_clubb_flx, exp_name, -4)

exp_name          = 'GOAIOP2_CLUBB_FLX'
path_goaiop2_clubb_flx  = './data/SCAM_GOAIOP2_FLX.cam.h0i.2014-09-01-01800.nc'
goaiop2_clubb_flx = down.data_load_xr(path_goaiop2_clubb_flx, exp_name, -4)



