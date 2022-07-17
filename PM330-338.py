import netCDF4 as nc
import matplotlib.pyplot as plt
from matplotlib.colors import from_levels_and_colors
import numpy as np
from matplotlib import animation
from matplotlib.colors import BoundaryNorm
import matplotlib.colors as cols
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from matplotlib import ticker, cm
import seaborn as sns

# each layer depth (m)
data1=nc.Dataset('/ihesp/user/xiliangdiao/ihespdata/ocn300/B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02.pop.h.0330-12.dz.nc')
lev1 = data1.variables['dz'][:]/100
#########
months = [f"{x:02d}" for x in range(1,13)]
years = [f"{x:04d}" for x in range(337,338)]
ii=0
result = np.zeros(600)

for yy in years:
    for mm in months:
        data=nc.Dataset('/scratch/user/xiliangdiao/firstpaper/UVEL_B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02.pop.h.'+yy+'-'+mm +'.nc')
        plotvar = data.variables['UVEL'][0,:,:]
        lont = data.variables['ULONG'][:400,1100]
        latt = data.variables['ULAT'][:400,1100]
##############################################
        plotvar[plotvar == -0.009999999776482582]= np.nan
        plotvar[plotvar == -1.0]= np.nan
        u = plotvar[:,:400,1100]
        u = u/100 # m/s
        u[u>0]=0
        #####  volume transport
        a = np.arange(0,399)
        A1= np.zeros([62,400])
        for j in a:
            A1[:,j] = u[:,j] * lev1[:] * (latt[j+1]-latt[j])*110.95 * 1000
        #####unit (m^3/s)
        A1[A1>100000000000000]=0
        final = np.nansum(A1)
        streamSV = final/1000000
        result[ii] = streamSV
        ii = ii + 1
        np.savetxt('/scratch/user/xiliangdiao/plot/PM337.out',result)