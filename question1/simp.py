import numpy as np

a = 1
b = 3
n = 11
h = (b - a) / (n )
x = np.linspace(a, b, n)
g= np.log(x)
f= x*np.log(x)-x

I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) \
            + 4*sum(f[1:n-1:2]) + f[n-1])


print(I_simp)

