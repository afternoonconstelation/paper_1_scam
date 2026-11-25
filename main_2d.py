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
import files_scam as scam

experiments=[
            scam.goaiop1_clubb_flx,
            scam.goaiop1_uw_flx, 
            ]

datei='2014-02-19T00'
datef='2014-02-19T23'

date =[
        [datei,datef],[datei,datef],
        ]

variables=['CLOUD']# ['CLOUDCOVER_CLUBB']

l1   =   [ 
            [f'CF Clubb var={variables[0]}'], #,f'(b)CF Bomex {variables[1]}'],
            [f'CF UW var={variables[0]}'],    #,f'(b)CF UW {variables[1]}'],
         ]

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

show            = [True]
#show            = [False]

tw.two_dimensional_exps_xr(experiments,variables,date,explabel1=l1,alt=alt,leg_loc=leg_loc,contour=cont,var_to=var2,color=color,show=show)
