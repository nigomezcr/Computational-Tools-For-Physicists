"""
Description: Exploration to the substactive cancelation in the solutions of ax^2 + bx + c = 0
"""
import numpy as np

def x1(a,b,c):
    return (-b + np.sqrt(b**2 - 4*a*c))/(2*a)

def x2(a,b,c):
    return (-b - np.sqrt(b**2 - 4*a*c))/(2*a)

def xp1(a,b,c):
    return -2*c/(b + np.sqrt(b**2 - 4*a*c))

def xp2(a,b,c):
    return -2*c/(b - np.sqrt(b**2 - 4*a*c))

def main():
    a, b = 1, 1

    N = 10
    print('Solutions to the quadratic equation with a=', a, ', b=', b, ', c = 10^(-n)')
    print('n', '    x_1    ', '     x_2     ', 
          '     x`_1    ', '    x`_2   ' )
    for n in range(1,N+1):
        c = pow(10,-n)
        print(n, "{0:.15f}".format(x1(a,b,c)),
                 "{0:.15f}".format(x2(a,b,c)),
                 "{0:.15f}".format(xp1(a,b,c)),
                 "{0:.15f}".format(xp2(a,b,c)) )
                
main()


"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Mar  14  2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""
