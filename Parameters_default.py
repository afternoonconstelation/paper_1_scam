import  os                                                           
from pathlib import Path

"""
@todo: change to yaml

"""

MODEL='SCAM'

plotdef='2d'

#Latex width 
wf=0.50
hf=1.0
cmmais=0.0

extend='both'

computer='/pesq'

UTC=-4

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# diretorio atual
#++++++++++++++++++++++++++++++++++++++++++++++++++++++

path =Path("./")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Out figure folder
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#new_path= Path('/pesq/dados/bamc/rardiles.branches/repositorio/scam_paper1/document')
new_path = path.resolve().parent.joinpath('document')
out_fig = new_path.joinpath('scam_figures')
out_table=path.joinpath('scam_table_files')
print(out_fig)
#out python nc files
out_files= path.joinpath('scam_nc_files')
 
os.makedirs(out_fig,exist_ok=True)
os.makedirs(out_table,exist_ok=True)
os.makedirs(out_files,exist_ok=True)     


