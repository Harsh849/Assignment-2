import sys
import numpy as np
import matplotlib.pyplot as plt
import math as m

import Twoainitial as ini
import funcforroots as rt


a=np.loadtxt("data.dat")
x=a[:,0]
y=a[:,1]


def F(x,a,b):
    n_div=100
    return ini.int_simpson(ini.f1,0,x,n_div,x,y)

nr_root=rt.NR_rt(F,ini.f1,-1,0.000001,x,y)
root_list=[nr_root]
x=-1
count=0
print("\nPart d")
while (x<=2):
    print("running...")             
    x+=nr_root+1
    if abs(nr_root - rt.NR_rt(F,ini.f1,x,0.000001,x,y))> 0.00001:
        nr_root=rt.NR_rt(F,ini.f1,x,0.000001,x,y)
        root_list.append(nr_root)






