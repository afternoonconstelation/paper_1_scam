# -*- coding: UTF-8 -*-
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# version by: Rardiles Branches
# using scam package developed by: Jhonatan A. A Manco
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Function to load the complete ncfiles  of regional MONAN run

from   scam  import data_own as down
from pathlib import Path
from glob import glob
import os

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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class ncdatasets():
    # adicionar funções para extrair apenas hora e as variáveis 
    def __init__(self,exp_flag:str='*CAM7*', main_file_folder:str='./data/ESM_data/archive',time_string:int='-4'):

        self.main_file_folder = main_file_folder
        self.exp_flag = exp_flag
        self.time_string = int(time_string)
        
    def _finder_scam_experiments(self):
        
        
        bamc_scam_dir = Path(self.main_file_folder) # make sure to be in the scam directory
        
        scam_list = glob(f'{self.exp_flag}',root_dir=bamc_scam_dir) # list all occurences of exp_flag in the experiments directory
        
        file_path = [bamc_scam_dir.joinpath(f'{i}').absolute() for i in scam_list] # recreates the path for each file in a list

        nc_file = [glob('*.nc',root_dir=file_path[i].joinpath('atm/hist/'))[0] for i,_ in enumerate(scam_list)]

        nc_path_files = [file_path[i].joinpath(f'atm/hist/{nc_file[i]}') for i,_ in enumerate(scam_list)]


        
        
        return nc_path_files,scam_list


    def load_datasets(self):
        exp_paths,exp_name = self._finder_scam_experiments()
        
        datasets={}
        
        for i,j in enumerate(exp_name):
            # down.data_load_xr(path to experiment, experiment name , time string)
            datasets[j]=down.data_load_xr(exp_paths[i],j,self.time_string)

        datasets_keys = list(datasets.keys())
        list_experiments = [datasets[i] for i in datasets_keys]
        return list_experiments 

    def labels_from_scam(self):
        _,exp_name = self._finder_scam_experiments()
        split_array = [i.split('_') for i in exp_name] 

        prtz=[]
        for i in split_array:
            
            # ------------------------------------------------
            # Paraterizations labels for automatic plottings
            # ------------------------------------------------  
            # stripped string with 2 tags
            #-------------------------------------------------

            if len(i)==2: # example: ['SCAM', 'ARM97']
               prtz.append("CLUBB")

            #-------------------------------------------------
            # stripped string with 3 tags
            #-------------------------------------------------
            elif len(i)==3: # ['SCAM', 'ARM97', 'UW']
               
               if i[2] not in ('FLX', 'CAM7'):
               
                   prtz.append(i[2])                    
               
               elif i[2] == 'CAM7' : # CLUBB modified

                   prtz.append('CLUBB modified')

               elif i[2] == 'FLX':  # Prescribed Fluxes

                   prtz.append('CLUBB Surf. Fluxes') 
            #------------------------------------------------- 
            # stripped string with 4 tags
            #-------------------------------------------------
            elif len(i)==4:
              
                if i[2] == 'CAM7' and i[3]=='FLX':
                    prtz.append(f'CLUBB modified (Surf. Fluxes)')
                else:
                   prtz.append(f'{i[2]} (Surf. Fluxes)')

                
        model = [i[0] for i in split_array]
        exp = [i[1] for i in split_array]            
        return model,exp,prtz