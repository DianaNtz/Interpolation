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
#create test function 1D
def f(z):
    return np.exp(-z**2)

zz=grid(zmin,zmax,N)
fzz=f(zz)
#1D Interpolation
def omega(zz):
    N=len(zz)
    w=np.zeros(N)
    for i in range(0,N):
        zi=zz[i]
        wi=1
        for j in range(0,i):
            wi*=zi-zz[j]
        for j in range(i+1,N):
            wi*=zi-zz[j]
        w[i]=1/wi
    return w
w=omega(zz)

def p(z,fzz):
    result=np.zeros(len(z))
    for i in range (0,len(z)):
       C1=0
       C2=0
       for j in range (0,len(w)):
          if(np.abs(z[i]-zz[j])<0.00001):
              C1=1
              C2=fzz[j]
              break
          else:
             C1=C1+w[j]/(z[i]-zz[j])
             C2=C2+w[j]/(z[i]-zz[j])*fzz[j]
       result[i]=C2/C1
    return result
