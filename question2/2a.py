# Lagrange Interpolation


import numpy as np
a=np.loadtxt("data.dat")
x=a[:,0]
y=a[:,1]
# Reading data points

n=len(x)

# Reading interpolation point
xp = float(input('Enter interpolation point: '))

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]    

# Displaying outputprint('Interpolated value at %.3f is %.3f.' % (xp, yp))
print(yp)
