# calczeta.py PYTHON program to calculate the cosmic ray ionisation rate
# Alice Eleanor Matthews

import numpy as np
import math

# constants all here for ease
pi = math.pi # 3.141... to high precision
br = 0.529*10**-10  # bohr radius in m
sigz = 6.51*10**-18 # sigma_zero const, page 28 Rudd, 1983

#print 'constants used in this program are as follows:'
#print 'pi', pi, 'bohr radius', br


# create an array of 90 energies from 1 - 9.0e+09
print('cosmic ray ionisation rate calculation')
count = 1
#en = []; # define en as a list
for i in range(1,10):
    for j in range(1,11):
        en = ([j*10**(i-1)])
        print(count, '{:.3e}'.format(en)
        count = count + 1
        xfac = en[k-1]/(1836/13.6)
        sigl = 4*pi*br**2*0.51*xfac**1.24
        print(sigl)
    
    nen = (count - 1)
    print('Number of energies = ', nen)

    #print(en)
    
    # CROSS SECTIONS
    # Proton contribution
    # REF: Rudd et al 1985 Rev Mod Phys, 57, 965
    # Equations 31, 32, 33 page 985
    #for k in range(1, nen):
    #    xfac = en[k-1]/(1836/13.6)
    #    sigl = 4*pi*br**2*0.51*xfac**1.24
    #    print(sigl)
    
    # Electron capture contribution
    # Rudd et al 1983 Phys Rev A 28 3244 page 28
    # Equation 19 
    # for i in range(1, nen):
    # xfac[i] = en[i]/(1836*15.42)
    # sigec = 1.044*sigz*2*15.42**(-2)*xfac[i]**2/(0.016+xfac[i]**2.88+0.136*xfac**5.86)
    