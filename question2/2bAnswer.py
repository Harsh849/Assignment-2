import sys
import numpy as np
import math as m

import Twoainitial as ini
import funcforroots as rt
import numpy as np
a=np.loadtxt("data.dat")
x=a[:,0]
y=a[:,1]
x_tol=0.0000001
x_start1=0
x_start2=3 

root1=rt.NR_rt(ini.f1,ini.Lagrandiff,x_start1,x_tol,x,y)
root2=rt.NR_rt(ini.f1,ini.Lagrandiff,x_start2,x_tol,x,y)

print("\nPart b")
print("The first root is: ",rt.NR_rt(ini.f1,ini.Lagrandiff,x_start1,x_tol,x,y))
print("The second root is: ",rt.NR_rt(ini.f1,ini.Lagrandiff,x_start2,x_tol,x,y))


