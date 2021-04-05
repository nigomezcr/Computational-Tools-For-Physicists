"""
Description: debugging example code 1
"""
import numpy as np
import matplotlib.pyplot as plt

def do_somethin(var):
    localvar = -1
    var[0] = 10
    sum1 = localvar + 5
    print(sum1)
    
a = [0]
print(a)

do_somethin(a)

print(a)





"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

