
import sys
import numpy as np
import matplotlib.pyplot as plt
import math as m

import Twoainitial as ini
import funcforroots as rt



a=np.loadtxt("data.dat")
x=a[:,0]
y=a[:,1]


coeff=ini.Lagrancoeff(x,y)

print("\nPart e")
print("The coefficient of x**0, x**1, x**2, x**3 are given by :\n",coeff)

global c1
c1 = coeff[0]
q1 = coeff[1]
q2 = coeff[2]
q3 = coeff[3]

def F_omsh(x,c,q1,q2,q3):

    return (c*x**3)/6 - 0.5*q1*x**2 + x*q2 - q3

def f_omsh(x,c,q1,q2,q3):

    return (c*x**2)/2 - x*q1 + q2 +0*q3

omega = rt.NR1_rt(F_omsh,f_omsh,0.2,0.00000001,c1,q1,q2,q3)
b1= q1 - c1*omega

a1 = q2 - (c1*omega**2)/2 -b1*omega

print("\nThe a,b,c,omega are: \n",[a1,b1,c1,omega])

