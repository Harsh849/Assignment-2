import numpy as np
n=100
def f(x):
     return x*np.log(x)-x
a=1
b=3
delx=(b-a)/n
sum=0
sum3=delx*((f(a)+f(b))/2)
for i in range(n):
        x1=a+i*delx
        sum=sum+f(x1)*delx

print(sum+sum3, "by trapezoidal")

