"""
Description: Exploration of Precision limit
"""

eps = 1.0
one = 1.0
N = 53

for n in range(N):
    eps /= 2.
    one = 1.0 + eps
    print(n, one, eps)




"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

