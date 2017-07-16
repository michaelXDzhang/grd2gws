# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:26:55 2017

@author: Benjamin Tsai
"""



WindSim_version = '441'
area_name = 'No25OffshoreWindFarm'
nxp = 600.
nyp = 600.
coordinate_system = '3'
xmin = 160267.56
xmax = 181455.29
ymin = 2660342.39
ymax = 2668833.35

import numpy
x = numpy.linspace(xmin,xmax,nxp)
y = numpy.linspace(ymin,ymax,nyp)
[xq,yq] = numpy.meshgrid(x,y)
rawdata = numpy.loadtxt('grdtest.grd')
points = rawdata[:,0:2].copy()
values = rawdata[:,2].copy()

from scipy.interpolate import griddata
zq = griddata(points, values, (xq, yq), method='nearest')
