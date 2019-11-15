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


file_open1 = open('AM.dat','r')

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
flux = np.array([]) # new array for flux
enV = np.array([100,200,300,400,500,600,700,800,900,1000])# new array for energy values in MeV
Zeta = np.array([2.1917174032190871E-015, 3.7399637076451944E-016,
        1.3221967884507738E-016, 6.3104137444882707E-017,
        3.5524498322903248E-017, 2.2205385921406979E-017,
        1.4920922930252911E-017, 1.0571379511208112E-017,
        7.7989338724564000E-018, 5.9401252468622789E-018])# new array for values of zeta

# Reading in the data and filling the array
#(en[i],sigp[i],sigec[i],sigtot[i],flux[i]))
(en,sigp,sigec,sigtot,flux) = read_data(file_open1)

# Plot cross section (all) vs  energy
fig1=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
plt.xlabel('Energy $[eV]$', fontsize = 20)
plt.ylabel('$\sigma_{proton}$ $ [ 1e^{-17} cm^{2} ]$', fontsize = 20)
plt.title('Cross section versus energy for proton impact on $H_2$ $(\epsilon = 400MeV)$\n', fontsize = 16)
plt.grid(True)
plt.plot(en,sigtot,color = 'r', marker = 'x', linestyle = '-', linewidth
         = 3.0, markersize = 4)

# Plot flux vs energy2
fig2=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
plt.xlabel('Energy $[eV]$', fontsize = 20)
plt.ylabel('$J_z(E,A/X) $[cm^{-2} s^{-1} sr{-1} (MeV/nucleon)^{-1}]$', fontsize = 20)
#plt.title('CR ionisation spectra $(\epsilon = 400MeV)$\n', fontsize = 16)
plt.grid(True)
plt.plot(en,flux,color = 'g', marker = 'x', linestyle = '-', linewidth= 3.0, markersize = 4,)


# Plot varying energy values with Zeta
fig3=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
plt.xlabel('$\epsilon$ $[eV]$', fontsize = 20)
plt.ylabel('$\zeta$ $ [s^{-1}]$', fontsize = 20)
#plt.title('Cosmic ray ionisation rate $\zeta$, for varying energies, E $(\epsilon = 400 MeV)$\n', fontsize = 16)
plt.grid(True)
plt.plot(enV,Zeta,color = 'k', marker = 'x', linestyle = '-', linewidth
         = 3, markersize = 8)
plt.hlines(y=2.19172*10**-15, xmin=100, xmax=1000, color = 'g', linestyle = '--', linewidth = 3) # adds horizontal lines on y axes corresponding to dense part of cloud
plt.hlines(y=5.94013*10**-18, xmin=100, xmax=1000, color = 'm', linestyle = '--', linewidth = 3)
plt.annotate(xy=[245,2.8*10**-15], s='Diffuse', color = 'g', fontsize = 20)
plt.annotate(xy=[245,9.5*10**-18], s='Dense', color = 'm', fontsize = 20)


# Plot cross section electron capture contribution
fig4=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
plt.xlabel('Energy $[eV]$', fontsize = 20)
plt.ylabel('$\sigma_ec$  $ [m^{2}]$', fontsize = 20)
#plt.title('Electron capture cross section contribution\nversus energy, E $(\epsilon = 400MeV)$\n', fontsize = 16)
plt.grid(True)
plt.plot(en,sigec,color = 'm', marker = 'x', linestyle = '--', linewidth
         = 3, markersize = 4)
#plt.axis([1000,1000000,0.1,140])

# Plot cross section electron capture and proton
fig5=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
plt.xlabel('Energy $[eV]$', fontsize = 20)
plt.ylabel('$\sigma_p$ $[m^{2}]$', fontsize = 20)
#plt.title('Electron capture $\sigma_{ec}$ (red), proton $\sigma_p$ (blue) and total $\sigma_{tot}$ (green) cross section\ncontribution versus energy, E $(\epsilon = 400MeV)$\n', fontsize = 16)
plt.grid(True)
plt.plot(en,sigec,color = 'r', marker = 'x', linestyle = '-', linewidth
         = 3, markersize = 4)
plt.annotate(xy=[19670.3,3.5e-17],s='$\sigma_{ec}$',color = 'r', fontsize = 20)
plt.plot(en,sigp,color = 'b', marker = 'x', linestyle = '-', linewidth
         = 3, markersize = 4)
plt.annotate(xy=[19670.3,3.5e-17],s='$\sigma_{p}$',color = 'b', fontsize = 20)
plt.plot(en,sigtot,color = 'g', marker = 'x', linestyle = '-', linewidth
         = 3, markersize = 4)
plt.annotate(xy=[9e6,8.8e-21],s='$\sigma_{tot}$',color = 'g', fontsize = 30)
plt.annotate(xy=[480,7.9e-25], s='$\sigma_{p}$', color = 'b', fontsize = 30)
plt.annotate(xy=[1e7,9e-27], s='$\sigma_{ec}$', color = 'r', fontsize = 30)
#plt.axis([1000,1000000,0.1,160])



# show all figures
plt.show()
