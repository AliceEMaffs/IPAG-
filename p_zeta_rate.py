# Alice Eleanor Matthews Edit from Pierre Hily Blant
# Code to calcualte the zeta and eta rate

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate
from scipy import special

#
# constants all here for ease
pi   = np.pi # 3.141... to high precision
br   = 0.529e-10  # bohr radius in m
sigz = 6.51e-18 # sigma_0 = 4*pi*br**2*I_H**2 where I_H = 13.6eV [m^2eV^2] Rudd 1983 pg 28

def nrj(e1,e2,nen):
    en = np.logspace(np.log10(e1),np.log10(e2),nen) # logarithmic array from 1 eV to 1 GeV
    return en

def sigma(en):
    #
    # Cross sections
    #
    # Proton contribution
    # Rudd et al 1985 Rev Mod Phys, 57, 965
    # Equations 31, 32, 33 page 985
    #
    # Electron capture contibution to cross section
    # Rudd et al 1983, physical review A, Volume 28, number 6
    # EC cross section equation 19 on page 3252 
    # Parameters A,B,C,D,F taken from Table VI for fitting equation 19
    # Values for I_i and N_i taken from Table II page 3251
    xfac = en/(1836*13.6)
    sigl = 4*pi*br**2*0.51*xfac**1.24 # low energy region Rudd+85 eqn 32
    sigh = 4*pi*br**2*(0.71*np.log(1.0+xfac)+1.63)/xfac # high energy region Rudd+85 eqn 33
    sigp = 1./(1./sigl + 1./sigh) # total proton contribution: Rudd+85 eqn 31
    xfac = en/(1836*15.42)
    sigec = sigz*1.044*2*15.42**-2*xfac**2/(0.016+xfac**2.88+0.136*xfac**5.86)
    return sigp,sigec

def lbmodel(en,eps):
    #
    # Returns the CR flux in particles cm^-2 s^-1 sr^-1 (MeV/nucleon)-1
    # Form parameter epsilon (in MeV) used to scale at low energies
    #
    # REF: C.J.Shen et al 2004
    # Checked against original source Webber & Yushak 1983
    # Equation 1, page 204
    # /!\ Energies en in Shen paper are in MeV
    const = 9.42e4 # Normalization const used for Flux  Shen et al 2004
    enmev = en*1e-6
    flux = const*enmev**0.3/(enmev+eps)**3
    return flux

def rate(sigma,flux,en):
    #
    # Compute the CR ionization rate
    #
    # Unit conversion
    # - convert sigma from m2 to cm2
    # - convert flux per (Mev/u) into flux per (eV/u)
    # CORRECTION FACTORS
    # 1. SECONDARY ELECTRON COEFFICIENT = phi
    # Chabot et al 2016 A&A 585, A15
    # Section 4 and 4.1 equations7,8,9,10
    # Accounting for ionisation of H2 by secondary electrons
    # Integral multiplied by the secondary electron factor 'sefac' - See constants
    # 2. CONTRIBUTION OF HEAVY NUCLEI CR's = eta
    # Padovani et al 2009 arXiv:0904.4149v1
    # Appendix A: Page 13
    # Accounting for th ionisation effects by heavy nuclei cosmic rays
    # Integral multiplied by the factor 'eta' - See constants
    func = flux*1e-6*sigma*1e4
    rate = 0
    for i in range(nen-1):
        rate += (func[i]+func[i+1])*(en[i+1]-en[i])*0.5
    phi = 1 + 0.7
    eta = 1 + 1.9
    zeta = 4*pi*phi*eta*rate
    return zeta

# Main
print('# Cosmic ray ionisation rate calculation')
nen=256
epsilon=400

en=nrj(1,1e9,nen)
sigp,sigec=sigma(en)
# Total proton contribution
sigtot = sigp + sigec
# Note: in Padovani+09, sigma in 1e-17 cm2: should x by 1e21
flux = lbmodel(en,epsilon)
zeta = rate(sigtot,flux,en)
print('# epsilon, zeta')
print epsilon,zeta


uo=open('AM.dat','w')
uo.write(("#%11s%12s%12s%12s%12s\n") % ("xen","sigp","sigec","sigtot","flux"))
uo.write(("#%11s%12s%12s%12s\n") % ("eV","m^2","m^2","m^2"))
uo.write("# Flux in cm-2 s-1 sr-1 (MeV/u)-1\n")
for i in range(nen):
      uo.write(("%12.3e%12.3e%12.3e%12.3e%12.3e\n") 
          % (en[i],sigp[i],sigec[i],sigtot[i],flux[i]))
uo.close()
