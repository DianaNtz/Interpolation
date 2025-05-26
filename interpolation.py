"""implementation of Barycentric Lagrange Interpolation in 1D and 2D"""
import numpy as np
import matplotlib.pyplot as plt
#create grid
zmin=0
zmax=np.pi
N=21

def grid(xmin,xmax,Nx):
     x=np.zeros(Nx)
     cx=(xmax-xmin)/2
     dx=(xmax+xmin)/2
     for j in range(0,Nx):
         x[j]=-np.cos(j*np.pi/(Nx-1))*cx+dx
     return x
