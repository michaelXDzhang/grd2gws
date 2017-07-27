# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:26:55 2017

@author: Benjamin Tsai
"""
import tkinter as tk
from tkinter import ttk
import glob as gb
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
for filename in gb.glob('./example/*.grd'):
    rawdata = np.loadtxt(filename)
    inpdata = np.vstack((inpdata, rawdata))
inpdata_min = inpdata.min(0)
inpdata_max = inpdata.max(0)

# define grid
x = np.linspace(min(xmin,inpdata_min[0]),max(xmax,inpdata_max[0]),nxp)
y = np.linspace(min(ymin,inpdata_min[1]),max(ymax,inpdata_max[1]),nyp)
#x = np.linspace(xmin,xmax,nxp)
#y = np.linspace(ymin,ymax,nyp)
[xq,yq] = np.meshgrid(x,y)
points = inpdata[:,0:2].copy()
values = inpdata[:,2].copy()

# grid the data
#zq = griddata(points, values, (xq, yq), method='nearest')
zq = griddata(points, values, (xq, yq), method='linear')
fill_value = 0
zq[np.isnan(zq)] = fill_value


CS = plt.contour(x, y, zq, 5, linewidths=0.5, colors='k')
CS = plt.contourf(x, y, zq, 5, vmax=abs(zq).max(), vmin=-abs(zq).max())
plt.colorbar()  # draw colorbar
plt.scatter(points[:,0], points[:,1], marker='o', s=5, zorder=10)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

#win = tk.Tk()
#win.mainloop()