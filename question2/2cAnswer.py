import sys
import numpy as np
import matplotlib.pyplot as plt
import math as m


import Twoainitial as ini

a=np.loadtxt("data.dat")
x=a[:,0]
y=a[:,1]
n=100
l_limit=0
u_limit=4

intgn= ini.int_simpson(ini.f1,l_limit,u_limit,n,x,y)
print("\nPart c")
print("The value  from 0 to 3 is: ", intgn)

