# Alice Eleanor Matthews
# Code for plotting zeta data
# cross sections
# flux
# zeta against energy
# file AM.dat reads in as (en[i],sigp[i],sigec[i],sigtot[i],flux[i]))
# import plotting library

import matplotlib.pyplot as plt

# import numpy for calculations
import numpy as np


file_open1 = open('AM_200.dat','r')
file_open2 = open('AM_400.dat','r')
file_open3 = open('AM_600.dat','r')
file_open4 = open('AM_plat.dat','r')


# for 5 columns
def read_data(file):
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]

    for line in file:
        line=line.split(' ')
#	print(line)
        for i in range(len(line)-1,-1,-1): # starts at end of line, ending at 0
            if line[i]=='':
                del line[i]
        line[1]=line[1].split('\n')[0]
        A.append(float(line[0]))#time
        B.append(float(line[1]))#H2O*
        C.append(float(line[2]))#O2
        D.append(float(line[3]))#O
        E.append(float(line[4]))#HH


    return A, B, C, D, E

en = np.array([]) # new array for energy in eV
sigp = np.array([]) # new array for cross section p
sigec = np.array([]) # new array for cross section p
sigtot = np.array([]) # new array for cross section p
flux2 = np.array([]) # new array for flux
flux4 = np.array([]) # new array for flux
flux6 = np.array([]) # new array for flux
fluxplat = np.array([]) # new array for flux


# Reading in the data and filling the array
#(en[i],sigp[i],sigec[i],sigtot[i],flux[i]))
(en,sigp,sigec,sigtot,flux2) = read_data(file_open1)
(en,sigp,sigec,sigtot,flux4) = read_data(file_open2)
(en,sigp,sigec,sigtot,flux6) = read_data(file_open3)
(en,sigp,sigec,sigtot,fluxplat) = read_data(file_open4)

# Plot flux vs energy2
fig2=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
plt.xlabel('Energy $[eV]$', fontsize = 20)
plt.ylabel('$J_z(E,A/X)$ $[cm^{-2} s^{-1} sr{-1}(MeV/nucleon)^{-1}]$', fontsize = 20)
#plt.title('CR ionisation spectra for values of $\epsilon = 200MeV, 400MeV, 600MeV$\n', fontsize = 16)
plt.grid(True)
plt.plot(en,flux2,color = 'r', marker = 'x', linestyle = '-', linewidth= 3.0, markersize = 4,)
plt.plot(en,flux4,color = 'b', marker = 'x', linestyle = '-', linewidth= 3.0, markersize = 4,)
plt.plot(en,flux6,color = 'g', marker = 'x', linestyle = '-', linewidth= 3.0, markersize = 4,)
plt.annotate(xy=[122000,5.14e-5],s='$\epsilon = 400MeV$',color = 'b', fontsize = 25)
plt.annotate(xy=[122000,1.98e-5],s='$\epsilon = 600MeV$',color = 'g', fontsize = 25)
plt.annotate(xy=[122000,8.5e-6],s='$\epsilon = 200MeV$',color = 'r', fontsize = 25)

# Plot flux vs energy2
fig2=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
plt.xlabel('Energy $[eV]$', fontsize = 20)
plt.ylabel('$J_z(E,A/X)$ $[cm^{-2} s^{-1} sr{-1}(MeV/nucleon)^{-1}]$', fontsize = 20)
#plt.title('CR ionisation spectra for values of $\epsilon = 200MeV, 400MeV, 600MeV$\n', fontsize = 16)
plt.grid(True)
plt.plot(en,fluxplat,color = 'r', marker = 'x', linestyle = '-', linewidth= 3.0, markersize = 4,)



# show all figures
plt.show()
