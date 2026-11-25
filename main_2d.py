#!/usr/bin/env python

"""
#################################
#################################
#PYTHON CODE TO PLOT DIFFERENTS 
#MAPS PROJECTION USING THE 
#LIBRARY BASEMAP. 
#################################
#PYTHON CODE TO PLOT DIFFERENS 
# Data:13/04/22
#################################
# By: Jhonatan A. A Manco
#################################
If you'd like your script to be more portable, consider finding the parent directory automatically:
"""

#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
####################################################
import os, sys

####################################################
#MAPS_PYTHON
####################################################
from  scam  import two_dimensional_xr as tw 

####################################################
from load_scam_bamc import ncdatasets
from   scam  import data_own as down


xxxxxxxxxx
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# scam runs from bamc directory 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# <MODEL>_<EXPERIMENT>_<PARAMETERIZATION*>
#
# * in case  of CLUBB parameterization, no flag is necessáry
# ------------------------------------------------------------------------------ 
# -- Convection Parametrizations
#
# UW        : University of Washigton parametrization (CAM5)
# --        : CLUBB (CAM6)
# CAM7      : CLUBB Modified (CAM7)    
#-------------------------------------------------------------------------------
# -- Experiments
#
# BOMEX     :
# SHAMZ     : Shallow convection GoAmazon
# GOAIOP1   : GoAmazon IOP 01
# GOAIOP2   : GoAmazon IOP 02

# FLX  : Prescribed Fluxes
# PUMAS: Microphysics PUMAS 
#--------------------------------------------------------------------------------
# usage: in the exp_flag, the given string should have the '*' to find the right pattern.
# example: *CAM7*  
# for all experiments, uses 'SCAM*'
scam=ncdatasets(exp_flag='*UW*', main_file_folder='./data/ESM_data/archive',
                time_string=-4)
experiments = scam.load_datasets()

# output informations to plot routines
model,exp,prtz = scam.labels_from_scam()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# @todo: to allow the script to distinguish the variable type (list, str or int)
# to use yaml.

datei='2014-02-19T00'
datef='2014-03-10T23'

date =[
        [datei,datef]#,[datei,datef],
        ]


experiments

#++++++++
#++++++++
#++++++++
#++++++++

variables=['CLOUD','VQ','VT']

l1 = [[f'{i} var = {variables[0]}'] for i in prtz ]


#-----------------------------------------------------------------------------------


alt     =   [
             [0,5.0],
             [0,5.0],
            ]
cont    =   [
              [0.01,25,11],
              [0.01,25,11],
            ]
var2    =   [100,100,1]
color   =   ['whbuyl','whbuyl','whbuyl']

#loc of legend and 
#size plot
size_wg         = 0.50
size_hf         = 0.60

ylabel          ='z [km]'
xlabel          ='Hours LT'
leg1            =( ['2014-02-19T01:00',5.1],[],['vertical',True,'%'],[xlabel,True],[ylabel,True ],[False],[size_wg,size_hf,1.33])
leg2            =( ['2014-02-19T01:00',5.1],[],['vertical',True,'%'],[xlabel,True],[ylabel,False],[False],[size_wg,size_hf,1.33])
leg3            =( ['2014-09-01T01:00',5.1],[],['vertical',True ,'%'],[xlabel,True],[ylabel,False],[False],[size_wg,size_hf,1.33])
leg4            =( ['2014-09-01T01:00',5.1],[],['vertical',True ,'%'],[xlabel,True],[ylabel,False],[False],[size_wg,size_hf,1.33])
leg_loc         =[
                    [leg1,leg1],
                    [leg1,leg1],
                 ]
print(leg_loc[1][1])

show            = [True]
#show            = [False]


tw.two_dimensional_exps_xr(experiments,variables,date),#explabel1=l1,alt=alt,#leg_loc=False,
                           #contour=cont,var_to=var2,color=color,show=show)

