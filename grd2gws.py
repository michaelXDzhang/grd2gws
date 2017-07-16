# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:26:55 2017

@author: Benjamin Tsai
"""
import os
import glob
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt


# define parameters
WindSim_version = '441'
area_name = 'No25OffshoreWindFarm'
nxp = 600
nyp = 600
coordinate_system = '3'
xmin = 160267.56
xmax = 181455.29
ymin = 2660342.39
ymax = 2668833.35

# import data
inpdata = np.array([0.,0.,0.])
for filename in glob.glob('.\example\*.grd'):
    rawdata = np.loadtxt(filename)
    inpdata = np.vstack((inpdata, rawdata))
inpdata = np.delete(inpdata, 0, 0)
ximax = inpdata.max(0)
ximin = inpdata.min(0)
# define grid
x = np.linspace(ximin[0],ximax[0],nxp)
y = np.linspace(ximin[1],ximax[1],nyp)
#x = np.linspace(xmin,xmax,nxp)
#y = np.linspace(ymin,ymax,nyp)
[xq,yq] = np.meshgrid(x,y)

#files = glob.glob('.\example\*.grd')
#rawdata = np.loadtxt('grdtest.grd')
points = rawdata[:,0:2].copy()
values = rawdata[:,2].copy()

# grid the data
zq = griddata(points, values, (xq, yq), method='nearest')

CS = plt.contour(xq, yq, zq, 5, linewidths=0.5, colors='k')
CS = plt.contourf(xq, yq, zq, 5,
                  vmax=abs(zq).max(), vmin=-abs(zq).max())
plt.colorbar()  # draw colorbar
plt.scatter(points[:,0], points[:,1], marker='o', s=5, zorder=10)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)