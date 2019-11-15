# Alice Eleanor Matthews
# Code for plotting ycalc data
# plotting the eta over zeta for LB and PS

# import plotting library
import matplotlib.pyplot as plt

# import numpy for calculations
import numpy as np


file_open1 = open('fort.76','r')
file_open2 = open('fort.33','r')

# for 2 columns
def read_data(file):
    X=[]
    Y=[]
   # Z=[]
    for line in file:
        line=line.split(' ')
	print(line)
        for i in range(len(line)-1,-1,-1): # starts at end of line, ending at 0
            if line[i]=='':
                del line[i]
        line[1]=line[1].split('\n')[0]
        X.append(float(line[0]))
        Y.append(float(line[1]))
       # Z.append(float(line[2]))

    return X, Y

en1 = np.array([]) # new array for energy1
ydat = np.array([]) # new array for cross section
atomno = np.array([]) # new array for atomic number Z
yld = np.array([]) # new array for yield 
enV = np.array([100,200,300,400,500,600,700,800,900])# new array for varying energy values
YRate = np.array([194.419, 29.566, 9.652, 4.336,	2.324, 1.394, 0.904, 0.621, 0.446])# new array for values of yield rate at corresponding energies as above
ZRate = np.array([2.1917174032190871E-015, 3.7399637076451944E-016, 1.3221967884507738E-016, 6.3104137444882707E-017, 3.5524498322903248E-017, 2.2205385921406979E-017, 1.4920922930252911E-017, 1.0571379511208112E-017, 7.7989338724564000E-018
])# new array for values of zeta rate at corresponding energies as above

# Reading in the data and filling the array
(en1, ydat) = read_data(file_open1)
(atomno, yld) = read_data(file_open2)

# Plot total rate vs varying energys 100-900
fig1=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xlabel('Varying energies (log) $[MeV]$', fontsize = 18)
plt.ylabel('$Y_{tot}$ (log) $[ H2O cm^{-2}s^{-1} ]$', fontsize = 18)
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
plt.xscale('log')
plt.yscale('log')
#plt.title('Total photo-desorption rate $Y_{tot}$, plotted against varying energies\n', fontsize = 16)
plt.grid(True)
plt.plot(enV, YRate, color = 'b', marker = 'x', linestyle = '-', linewidth
         = 2, markersize = 8,)
plt.axis([100,900,0.1,1000])

# Plot total Y rate vs Z
fig2=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xlabel('Atomic number, $Z$', fontsize = 18)
plt.ylabel('$Y_{tot}$ $[ H2O cm^{-2}s^{-1} ]$', fontsize = 18)
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
#plt.title('Total photo-desorption yield $Y_{tot}$, plotted against\natomic number Z\n', fontsize = 16)
plt.grid(True)
plt.plot(atomno, yld, color = 'k', marker = 'x', linestyle = '--', linewidth
         = 3, markersize = 8,)


# Plot total Y rate vs Zeta rate for varying energys 100-900
fig3=plt.figure(num=None, figsize=(10,8), dpi = 100, facecolor='w', edgecolor='k')
plt.xlabel('$\zeta$ (log) $[s^-1]$', fontsize = 18)
plt.ylabel('$Y_{tot}$ (log) $ [ H2O cm^{-2}s^{-1} ]$', fontsize = 18)
plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis = 'x', labelsize = 16)
plt.tick_params(axis = 'y', labelsize = 16)
#plt.title('Total photo-desorption yield $Y_{tot}$, plotted against\ncosmic ray ionisation rate $\zeta$, \nshowing their values for dense clouds (pink) and diffuse clouds (green)', fontsize = 16)
plt.grid(True)
plt.plot(ZRate, YRate, color = 'k', marker = 'x', linestyle = '-', linewidth = 2, markersize = 8)
plt.axis([7.7989338724564000*10**-18, 2.1917174032190871*10**-15,0.446, 194.419]) # adds limits to x and y axis so fits data points
plt.vlines(x=3*10**-17, ymin=0.446, ymax=1.9337, color = 'm', linestyle = '-', linewidth = 2) # adds vertical lines on x axes corresponding to dense part of cloud
plt.vlines(x=5*10**-16, ymin=0.446, ymax=40.282, color = 'g', linestyle = '-', linewidth = 2) # adds vertical lines on x axes corresponding to diffuse part of cloud
plt.hlines(y=1.9337, xmin=7.7989338724564000*10**-18, xmax=3*10**-17, color = 'm', linestyle = '-', linewidth = 2) # adds horizontal lines on y axes corresponding to dense part of cloud
plt.hlines(y=40.282, xmin=7.7989338724564000*10**-18, xmax=5*10**-16, color = 'g', linestyle = '-', linewidth =2) # adds horizontal lines on y axes corresponding to diffuse part of cloud
plt.annotate('dense cloud\n(3E-17, 1.9337)', xy=(4.77*10**-17,1.8), color = 'm', fontsize = 20)
plt.annotate('diffuse cloud\n(5E-16, 40.282)', xy=(7.7*10**-17,43.1), color = 'g', fontsize = 20)

# show all figures
plt.show()
