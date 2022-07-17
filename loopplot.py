# first plot

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
months = [f"{x:02d}" for x in range(1,13)]
years = [f"{x:04d}" for x in range(116,127)]
i =0
for yy in years:
    for mm in months:
        data=nc.Dataset('/ihesp/xiliangdiao/ihespdata/ice/hist/B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02.cice.h.'+yy+'-'+mm +'.icearea.nc')
        plotvar = data.variables['aice'][0,:,:]
        lont = data.variables['lont_bounds'][:,:,0]
        latt = data.variables['latt_bounds'][:,:,0]

        # Pick some of the nicer colors from the palette...
        nice_cmap=plt.get_cmap('ocean')
        lev_cmap = nice_cmap([5,130,150,175,200,210,240])
        new_cmap = cols.ListedColormap(lev_cmap,"praj_cmap")
        nice_levels = [0,15,40,80,90,95,100]
        norm = mpl.colors.BoundaryNorm(nice_levels, new_cmap.N)
#********************************************************************
        plt.figure(figsize=(20,20))
        my_font = {'fontname':'Cambria', 'size':'20'}

        map=Basemap(projection='spstere',lon_0=180,boundinglat=-50,resolution='h')
        map.drawparallels(np.arange(-80,80,10),labels=[1,0,0,0],fontsize=14)
        map.drawmeridians(np.arange(-180,180,30),labels=[0,0,1,1],fontsize=14)
        map.drawmapboundary(color='black')
        map.fillcontinents(color='white')
        map.drawcoastlines()
        x,y=map(lont,latt)
        CP = map.contourf(x,y,plotvar,range(0,100),cmap = new_cmap,norm =norm,spacing = 'uniform',\
                  levels = nice_levels)

        #CP = map.contourf(x,y,plotvar,vmin = 0.000000001, vmax = 100, cmap=new_cmap)
        cbar =map.colorbar(CP,extend='both',extendfrac='auto',extendrect='True')
        cbar.ax.tick_params(labelsize=15)
        i= i+1
        plt.suptitle('SEA ICE AREA'+yy+'-'+mm,**my_font)
# it is important to save the images in a very sequential manner or ffmpeg will not work !!!
        #plt.savefig('aice'+y +'-' + m+ '.png')
        plt.savefig("/scratch/user/xiliangdiao/plot/video1/PSP_%04d.png"%(i))
