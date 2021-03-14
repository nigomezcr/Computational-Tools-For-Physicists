"""
Description: Complex numbers and functions in Python
"""
import numpy as np
import cmath as cm
import matplotlib.pyplot as plt


print("phi", "\t", " x ", " y ", "  e  ", "  ln  ", "  sqrt  ", "  atan  ")
print("--------------------------------------------------------")

for phi in np.arange(-4*np.pi, 4*np.pi, 0.25*np.pi):
    #Compute phase and norm
    r = 1

    #Declare complex number
    z = r*cm.exp(phi*1j)

    #Compute imaginary and real parts
    x = z.real
    y = z.imag

    #Compute functions
    e = cm.exp(z)
    ln = cm.log(z)
    root = cm.sqrt(z)
    atan = np.arctan(y/x)

    print(round(phi,2), round(x,2), round(y,2), e, ln, root, round(atan,2))


#Now, lets define vectors for making plots of the phase
InputPhases = np.arange(-4*np.pi, 4*np.pi, 0.25*np.pi)


AtanPhases = np.zeros(32)
for i in np.arange(32):
    r = 1
    z = r*cm.exp(InputPhases[i]*1j)
    x = z.real
    y = z.imag
    AtanPhases[i] = np.arctan(y/x)
    #print(InputPhases[i], AtanPhases[i])    

plt.title('Input phases vs atan')
plt.xlabel('input $\phi$')
plt.ylabel('$atan(y/x)$')

plt.plot(InputPhases,AtanPhases, 'y')    
plt.savefig('phases_py.pdf')    
    
    
"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Mar  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

    
