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
from sklearn import linear_model

data1 = np.loadtxt("/ihesp/fudan1991/pub/GlobalSST_0021_0501.txt")
SST = data1[130:480]

aaa = np.load('AICE.npy')
aice = aaa[130:480,0:10,:]


res = np.zeros([10,360])

lon = np.arange(0,10)
lat = np.arange(0,360)

for item in enumerate(lon):
    for jtem in enumerate(lat):
        plotvar = aice[:,item,jtem]
        if plotvar < 1000:
            regr = linear_model.LinearRegression()
            regr.fit(SST.reshape(-1, 1), plotvar)
            a = regr.coef_
            res[item,jtem]=a
        else:
            res[item,jtem]=np.nan
    np.savetxt('AICE10.out',res)
    
