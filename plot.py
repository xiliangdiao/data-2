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

data=nc.Dataset('/scratch/user/xiliangdiao/600aice.nc')
plotvar = data.variables['aice'][0,:,:]
lont = data.variables['lont_bounds'][:,:,0]
latt = data.variables['latt_bounds'][:,:,0]

# Pick some of the nicer colors from the palette...
nice_cmap=plt.get_cmap('ocean')
lev_cmap = nice_cmap([5,100,130,170,200,230,240]) 
new_cmap = cols.ListedColormap(lev_cmap,"praj_cmap")
nice_levels = [0,15,40,80,96,98,100]
norm = mpl.colors.BoundaryNorm(nice_levels, new_cmap.N)
#********************************************************************
plt.figure(figsize=(20,20))
my_font = {'fontname':'Cambria', 'size':'20'}

map=Basemap(projection='spstere',lon_0=180,boundinglat=-50,resolution='l')
map.drawparallels(np.arange(-80,80,10),labels=[1,0,0,0],fontsize=14)
map.drawmeridians(np.arange(-180,180,30),labels=[0,0,1,1],fontsize=14)
map.drawmapboundary(color='black')
map.fillcontinents(color='white')
map.drawcoastlines()
x,y=map(lont,latt)
CP = map.contourf(x,y,plotvar,locator=ticker.LogLocator(),vmin = 0.000000001, vmax = 100, cmap=new_cmap)
cbar =map.colorbar(CP,extend='both',extendfrac='auto',extendrect='True')
cbar.ax.tick_params(labelsize=15) 
#plt.suptitle("SEA ICE CONCENTRATION (aggregate) \n Simulation Year %d-Month %d"%(sicyear[i],sicmonth[i]),**my_font)
# it is important to save the images in a very sequential manner or ffmpeg will not work !!!
plt.savefig("aice.png")
