"""
Multiplicative errors
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import special


def myBessel(l,x):
    L = 25
    JL = special.spherical_jn(L,x)
    JL1 = special.spherical_jn(L+1,x)
    
    
    for i in np.arange(L,l,-1):
        myJ = (2*i + 1)*JL/x - JL1
        JL1 = JL
        JL = myJ
    return myJ


def main():
    x = 1
    l = 24
    
    BesselArray = np.zeros(l+1)
    MyArray = np.zeros(l+1)
    D = np.zeros(l+1)
    L = np.arange(l,-1,-1)
    
    print(' l ', '   myJ(l,x)    ', '     J(l,x)  ', '   |muJ - J|    ')
    for n in L:
        BesselArray[n] = special.spherical_jn(n,x)
        MyArray[n] = myBessel(n, x)
        D[n] = abs(myBessel(n,x) - special.spherical_jn(n,x) )
        print(n,  
              MyArray[n], 
              BesselArray[n],
              D[n]
              )
        
    L.sort()
    
    plt.xlabel('$n$')
    plt.ylabel('$|j_n{rec} (^x) - j_n^{built}(x)|$')
    plt.title('Multiplicative Errors with Bessel functions')
    
    plt.loglog(L,D,'-*')
    plt.savefig("bessel_py.pdf")
    
    
main()

