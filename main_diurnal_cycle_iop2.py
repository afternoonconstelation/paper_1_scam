#!/usr/bin/env python

"""
#################################
#################################
#PYTHON CODE TO PLOT DIFFERENS 
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

import matplotlib.pyplot as plt

####################################################
#MAPS_PYTHON
####################################################
from   scam  import temporal_plot as tp

####################################################
import files_scam as scam

###import Parameters_clf as obs

import plotparameters as plotpara

exp=[
            scam.goaiop2_clubb_flx,
            scam.goaiop2_uw_flx,
            ]

#print(scam.goaiop2_clubb.time)

explabel1     = [
                    r'CLUBB',
                    r'CLUB_FLX',
                    r'UW',
                    r'UW_FLX',
               ] 

color       =  [
                'orange',
                'blue',
                'red',
                'green',
               ]

nameplot='GOA_IOP2'

var     =  ['PRECT','SHFLX','LHFLX','TGCLDIWP']
#TGCLDIWP:units = "kg/m2" ;
#TGCLDIWP:long_name = "Total grid-box cloud ice water path" 

hi='00:00'
hf='23:00'

date1i=f'2014-02-15T{hi}'
date1f=f'2014-03-20T{hi}'
date2i=f'2014-09-01T{hi}'
date2f=f'2014-10-10T{hi}'
#datef=f'2014-10-08T{hf}'
date =[
        [f'{date2i}',f'{date2f}',2],
        [f'{date2i}',f'{date2f}',2],
        [f'{date2i}',f'{date2f}',2],
        [f'{date2i}',f'{date2f}',2],
        ]


date_obs =[
            [f'{date2i}',f'{date2f}',2],
            [f'{date2i}',f'{date2f}',2],
            [f'{date2i}',f'{date2f}',2],
            [f'{date2i}',f'{date2f}',2],
          ]

var_to      =  [
                1,1,1,1,
               ]


lim         =  [0,24,4] 

a0=(0,1.0,4)
a1=(0,200.0,4)
a2=(0,400.0,4)
a3=(0,0.2,4)

alt         =  [
               a0,a1,a2,
               a3,a1,a2,
               ]


line    =   [
                [1,0]    ,
                [1,0]    ,
                [1,0]    ,
                [1,0]    ,
            ]


s1=[True,True,True]
show       =  [ s1,s1,s1,s1,s1,s1,
               ]

X           =  'Hours'
#X           = 'Horas HL'
Y0          =  r'Precipitation  [mmhr$^{-1}$]'
Y1          =  r'SHF $\mathrm{ [W m^{-2}]}$'
Y2          =  r'LHF $\mathrm{ [W m^{-2}]}$'
Y3          =  r'Liquid Water Path $\mathrm{ [kg m^{-2}]}$'
Y4          =  r'Liquid Water Path [kg/m${^2}$]'
Y5          =  'W Maximum [m/s]'
Y6          =  r'CAPE [Jkg$^{-1}$]'
Y7          =  r'CIN  [Jkg$^{-1}$]'


datep=14
l0          =  [[X,Y0],['',datep,0 ]  ,[True,'upper right'],[0.5,0.5,0]]
l1          =  [[X,Y1],['',datep,635 ],[True,'upper right'],[0.5,0.5,0]]
l2          =  [[X,Y2],['',datep,305 ],[True,'upper right'],[0.5,0.5,0]]
l3          =  [[X,Y3],['',datep,0.11],[True,'upper right'],[0.5,0.5,0]]
l4          =  [[X,Y4],['',datep,0.11],[True,'upper left'],[0.5,0.5,0]]
l5          =  [[X,Y5],['',datep,0.11],[True,'upper left'],[0.5,0.5,0]]
l6          =  [[X,Y6],['',datep,0.11],[True,'lower center'],[0.5,0.5,0]]
l7          =  [[X,Y7],['',datep,0.11],[True,'upper left'],[0.5,0.5,0]]


plot_def    =  [
                l0,l1,l2,l3,
                l4,l5,l6,l7
                ]

var_obs      =  ['prec_srf','SH','LH','LWP']
#LWP cm to gr/cm
#cm*(density of water=1 gr/cm^3)= gr/cm^2=10000cm^2/m^2=gr/m^2*10000*1kg/1000gr
var_to_obs   =  [1,1,1,1*10] 

sv=True

tp.temporal_diurnal_cycle_var_exp(
                exp,date=date,variables=var,explabel1=explabel1,explabel2=explabel1,
                alt=alt,color=color,line=line,var_to=var_to,plot_def=plot_def,
                #obs=obs.prec1_rd,date_obs=date_obs,var_obs=var_obs,var_to_obs=var_to_obs,
                #obs2=obs.prec1_tr,date_obs2=date_obs,var_obs2=var_obs,var_to_obs2=var_to_obs,
                show=show,save=[sv,nameplot],date0=[1,1,2026],lim=lim,plotpara=plotpara)
