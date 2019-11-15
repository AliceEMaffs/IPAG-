# calczeta.py PYTHON program to calculate the cosmic ray ionisation rate
# Alice Eleanor Matthews

import numpy as np
import math

# constants all here for ease
pi = math.pi # 3.141... to high precision
br = 0.529*10**-10  # bohr radius in m

#print 'constants used in this program are as follows:'
#print 'pi', pi, 'bohr radius', br


# create an array of 90 energies from 1 - 9.0e+09
print('cosmic ray ionisation rate calculation')
count = 1
zen = [] # define en as a list
for i in range(1,10):
    for j in range(1,11):
        en.append(j*10**(i-1))
        print(count, '{:.3e}'.format(en[count-1])
        count =+ count + 1
        
    nen = (count - 1)
    print('Number of energies = ', nen)

    # CROSS SECTIONS
    # Proton contribution
    # REF: Rudd et al 1985 Rev Mod Phys, 57, 965
    # equations 31, 32, 33 page 985
    #for k in range(1, nen):
    #    xfac = en[k-1]/1836/13.6 
    #    sigl = 4*pi*br**2*0.51*xfac**1.24
    #    print(sigl)
    
    
    print(en)