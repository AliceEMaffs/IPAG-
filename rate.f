c     rate_xsec.f
      
c     this program has been editied to save all the cross sections
c     separately in order to separately plot them on a graph
      
      program rate
      implicit none
      integer, parameter :: np=1000
      real*8 flux(np), Sn(np), Se(np), en(np), test(np)
      real*8 yd(np), tau
      real*8 emin, emax
      real*8 mass, int, int2, dep, ksi
      real*8 sigma(np),sigl(np),sigh(np), sigec(np)
      real*8 :: xfac
      integer i, j, k, io, nen, cpt
c
      real*8, parameter :: pi=acos(-1.d0)
      real*8, parameter :: a0=0.529d-10  ! [   m] Bohr radius 
      real*8, parameter :: sig0=6.51e-18 ! [m^2 eV^2]

c
c     rho=1.52 g.cm-3 for PEG material
c     M=6.31 g.mol-1 for PEG material
c     Na=6.02e23 Avogadro number
c
      real*8, parameter :: rho=1.1d0
      real*8, parameter :: M=6.31d0
      real*8, parameter :: Na=6.02d23
c     
c     E0=400 MeV, from Shen et al. (2004)
c     C=9.42e4, from Shen et al. (2004)
c     
      real*8, parameter :: E0=400.d0
      real*8, parameter :: C=9.42d4
c     
c     set up the energy grid in eV
c      
      cpt=1
      do i=1,10
         do j=1,9
            en(cpt)=dble(j*10.d0**(i-1))
            write(6,'(i5,e12.3)') cpt, en(cpt)
            cpt=cpt+1
         enddo
      enddo

      nen=cpt-1
      
      write(6,*) 'Number of energies'
      write(6,*) nen
c
c     ionization cross section from Rudd et al. Rev. Mod. Phys. 57 965 (1985)
c     as employed in Padovani et al. (2009)
c     
c     Alice edited code
      
      do i=1,nen

         sigl(i)=4*pi*a0**2*0.51d0*(en(i)/1836.d0/13.6d0)**1.24d0
         sigh(i)=4*pi*a0**2*(0.71d0*log(1+en(i)/1836.d0/13.6d0)+1.63d0)
     $        /(en(i)/1836.d0/13.6d0)
         
C     Electron capture cross-section for proton impact on H2
C     Rudd et al 1983 Phys Rev A 28 6, Eq 19, Table VI and VII
C     Cross-checked against Padovani et al 2009
         xfac = en(i)/1836./15.42
         sigec(i) = sig0*1.044*2/15.42**2*xfac**2/
     $        (0.016+xfac**2.88+0.136*xfac**5.86)
        
c        original proton sigma         
         sigma(i)=1.d0/(1.d0/sigl(i)+1.d0/sigh(i))

c     save the proton cross section as separate file converted to cm^2
         write(166,'(3e12.3)')sigma(i)*1.d21

c     save the electron cross section as separate file converted to cm^2
         write(366,'(3e12.3)')sigec(i)*1.d21

c        new sigma
         sigma(i) = sigma(i) + sigec(i)
         
c      save the sunm of cross sections as separate file converted to cm^2     
         write(566,'(3e12.3)') en(i),sigma(i)*1.d21
         
c     sigma converted from m2 to 1e-17 cm2 as in Padovani et al. (2009)
         
c        original sigma
c     write(66,'(2e12.1)') en(i), sigma(i)*1.d21

         write(66,'(3e12.3)') en(i),sigma(i)*1.d21,sigec(i)*1.d21
         
      enddo

      
      do i=1,nen
c     
c     energy in MeV/nucleon in Shen et al. (2004), flux converted to eV
c     here
c     
         flux(i)=(C*(en(i)*1.d-6)**0.3)/(en(i)*1.d-6+E0)**3*1.d-6
         
         write(77,'(2e12.3)') flux(i)
         
      enddo
c     
c     integral with trapezoidal rule
c     
            
      int = 0.d0 
      
      do i=2,nen
c     
c     sigma converted from m2 to cm2
c     
         sigma(i)=sigma(i)*1e4

c         sigma(i)=pi*(0.1d-4)**2

         int= int + (flux(i-1)*sigma(i-1) + flux(i)*sigma(i))/2.d0
     $        *(en(i)-en(i-1))
         
      enddo

      ksi = 4*pi*int 
      
c     
c     correction for heavy nuclei (1+1.9)
c     + correction for secondary electrons
c     see Chabot et al. (2016)
c     
      ksi = ksi*(1+1.9)*(1+0.7)
      
c     Fe abundance= 713/1.d6 
c      ksi = ksi*713.d0/1.d6

      
c      write(6,*) 'Integral'
c      write(6,*) int

      write(6,*) 'Rate (s-1)'
      write(6,*) ksi
      
      end
      
         
      