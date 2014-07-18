# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pylab as pl
import math
import sympy as sy
from mpl_toolkits.mplot3d import axes3d # for 3D graphing

# <codecell>

# Coil variables
mu = 4.0 * np.pi * 10**(-7) # (T)
coilSideLength = 1  # side length of coil (m)
coilSeparation = 1.089 * coilSideLength  # ideal separation for square coils (m)
current = 1  # in Amps

# <codecell>

# Coils are preresented as 2 xy-planes, with x pointing up, y pointing out of page, and z pointing right.
x = np.linspace(-coilSideLength,coilSideLength)
y = np.linspace(-coilSideLength,coilSideLength)
z = np.linspace(-(coilSeparation/2.0), coilSeparation/2.0)

# <markdowncell>

# ## Magnetic Field Components

# <markdowncell>

#     Based on Li, Thomas Tsz-Ka. "Tri-axial Square Helmholtz coil for Neutron EDM Experiemnt". August 25, 2004.

# <codecell>

def ByComponent(x,y,z,l,d,I):
    """By output in tesla.  Input x,y,z, side length(l), separation(d), current(I)"""
    a = l/2.0  # or = l/2.0?
    A = (x+a)
    B = (z - d/2.0)
    C = (y-a)
    D = (y+a)
    E = (x-a)
    F = (z + d/2.0)
    By = ((mu*I)/(4*np.pi)) * ( ((A*B) / ((C**2 + B**2)*np.sqrt(A**2+C**2+B**2))) - ((A*B) / ((D**2 + B**2)*np.sqrt(A**2+D**2+B**2))) + ((E*B) / ((D**2 + B**2)*np.sqrt(E**2+D**2+B**2))) - ((E*B) / ((C**2 + B**2)*np.sqrt(E**2+C**2+B**2))) + ((A*F) / ((C**2 + F**2)*np.sqrt(A**2+C**2+F**2))) - ((A*F) / ((D**2 + F**2)*np.sqrt(A**2+D**2+F**2))) + ((E*F) / ((D**2 + F**2)*np.sqrt(E**2+D**2+F**2))) - ((E*F) / ((C**2 + F**2)*np.sqrt(E**2+C**2+F**2))) )
    return By

# <codecell>

def BxComponent(x,y,z,l,d,I):
    """Bx output in tesla.  Input x,y,z, side length(l), separation(d), current(I)"""
    a = l/2.0  # or = l/2.0?
    A = (x+a)
    B = (z - d/2.0)
    C = (y-a)
    D = (y+a)
    E = (x-a)
    F = (z + d/2.0)
    Bx = ((mu*I)/(4*np.pi)) * ( ((D*B) / ((E**2 + B**2)*np.sqrt(E**2+D**2+B**2))) - ((D*B) / ((A**2 + B**2)*np.sqrt(A**2+D**2+B**2))) + ((C*B) / ((A**2 + B**2)*np.sqrt(A**2+C**2+B**2))) - ((C*B) / ((E**2 + B**2)*np.sqrt(E**2+C**2+B**2))) + ((D*F) / ((E**2 + F**2)*np.sqrt(E**2+D**2+F**2))) - ((D*F) / ((D**2 + F**2)*np.sqrt(A**2+D**2+F**2))) + ((C*F) / ((D**2 + F**2)*np.sqrt(A**2+C**2+F**2))) - ((C*F) / ((E**2 + F**2)*np.sqrt(E**2+C**2+F**2))) )
    return Bx

# <codecell>

def BzComponent(x,y,z,l,d,I):
    """Bz output in tesla.  Input x,y,z, side length(l), separation(d), current(I)"""
    a = l/2.0  # or = l/2.0?
    A = (x+a)
    B = (z - d/2.0)
    C = (y-a)
    D = (y+a)
    E = (x-a)
    F = (z + d/2.0)
    Bz = ((mu*I)/(4*np.pi)) * ( ((A*D) / ((D**2 + B**2)*np.sqrt(A**2+D**2+B**2))) + ((A*D) / ((A**2 + B**2)*np.sqrt(A**2+D**2+B**2))) - ((A*C) / ((C**2 + B**2)*np.sqrt(A**2+C**2+B**2))) - ((A*C) / ((A**2 + B**2)*np.sqrt(A**2+C**2+B**2))) - ((E*D) / ((E**2 + B**2)*np.sqrt(E**2+D**2+B**2))) - ((E*D) / ((D**2 + B**2)*np.sqrt(E**2+D**2+B**2))) + ((E*C) / ((E**2 + B**2)*np.sqrt(E**2+C**2+B**2))) + ((E*C) / ((C**2 + B**2)*np.sqrt(E**2+C**2+B**2))) + ((A*D) / ((D**2 + F**2)*np.sqrt(A**2+D**2+F**2))) + ((A*D) / ((A**2 + B**2)*np.sqrt(A**2+D**2+B**2))) - ((A*C) / ((C**2 + F**2)*np.sqrt(A**2+C**2+F**2))) - ((A*C) / ((A**2 + F**2)*np.sqrt(A**2+C**2+F**2))) - ((E*D) / ((E**2 + F**2)*np.sqrt(E**2+D**2+F**2))) - ((E*D) / ((D**2 + F**2)*np.sqrt(E**2+D**2+F**2))) + ((E*C) / ((E**2 + F**2)*np.sqrt(E**2+C**2+F**2))) + ((E*C) / ((C**2 + F**2)*np.sqrt(E**2+C**2+F**2))) )
    return Bz

# <codecell>

#def BzComponent(z,l,d,I):
#    """Bz output in tesla.  Input z, separation(d), side length(l), and current(I)."""
#    a = l # Not sure based on paper
#    Bz = ((2*mu*I*(l**2))/np.pi) * ( (1/(a**2 + (z-d/2.0)**2)*(np.sqrt(2*a**2 + (z-d/2.0)**2))) + (1/(a**2 + (z-d/2.0)**2)*(np.sqrt(2*a**2 + (z-d/2.0)**2))) )
#    return Bz

# <markdowncell>

# ### Calculating By component and plotting along y-axis

# <codecell>

xx, zz = np.meshgrid(x,z)  # For looking at By component (x-z plane)
#print xx, zz

ByField = ByComponent(xx,y,zz,coilSideLength,coilSeparation,current)
#print ByField
pl.plot(y,ByField, label="By")
pl.xlabel("y (m)")
pl.ylabel("By Field (T)")
pl.title("By Component Along Y")
#pl.legend(loc='upper right')
pl.show()

# <markdowncell>

# ### Calculating Bz component and plotting along z-axis

# <codecell>

xx, yy = np.meshgrid(x,y)  # For looking at Bz component (x-y plane)
BzField = BzComponent(xx,yy,z,coilSideLength,coilSeparation,current)
#print BzField

# <codecell>

pl.plot(z,BzField, label="Bz")
pl.xlabel("z (m)")
pl.ylabel("Bz Field (T)")
pl.title("Bz Component Along z")
#pl.legend(loc='upper right')
pl.show()

# <markdowncell>

# ### Calculating Bx component and plotting along x-axis

# <codecell>

yy, zz = np.meshgrid(y,z)  # For looking at Bx component (y-z plane)
#print yy, zz

BxField = BxComponent(x,yy,zz,coilSideLength,coilSeparation,current)
#print BxField
pl.plot(y,BxField, label="Bx")
pl.xlabel("x (m)")
pl.ylabel("Bx Field (T)")
pl.title("Bx Component Along X")
#pl.legend(loc='upper right')
pl.show()

# <markdowncell>

# ###Contour plots

# <codecell>

# Almost correct

# <codecell>

CS = pl.contour(y, z, BxField)
pl.xlabel("y (m)")
pl.ylabel("z (m)")
pl.clabel(CS,inline=True,fmt='%1.1e',fontsize=10)
pl.title('Bx Field Contour')
pl.show()

# <codecell>

CS1 = pl.contour(x, z, ByField)
pl.xlabel("x (m)")
pl.ylabel("z (m)")
pl.clabel(CS1,inline=True,fmt='%1.1e',fontsize=10)
pl.title('By Field Contour')
pl.show()

# <codecell>

CS2 = pl.contour(x, y, BzField)
pl.xlabel("x (m)")
pl.ylabel("y (m)")
pl.clabel(CS2,inline=True,fmt='%1.1e',fontsize=10)
pl.title('Bz Field Contour')
pl.show()

# <codecell>


