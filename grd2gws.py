# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:26:55 2017

@author: Benjamin Tsai
"""

import numpy as np

WindSim_version = '441'
area_name = 'No25OffshoreWindFarm'
nxp = 600.
nyp = 600.
coordinate_system = '3'
xmin = 160267.56
xmax = 181455.29
ymin = 2660342.39
ymax = 2668833.35

x = np.linspace(xmin,xmax,nxp)
y = np.linspace(ymin,ymax,nyp)
[xq,yq] = np.meshgrid(x,y);
rawdata = np.loadtxt('grdtest.grd')



