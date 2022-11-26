import numpy as np

def f1(x,a,b):
    
    l=1
    sum=0
    for j in range(len(a)):

        l=1

        for i in range(len(a)):
            if j==i:
                continue
            l*= (x-a[i])/(a[j]-a[i])

        sum+= b[j]*l
    

    return sum
    


    
def Lagrandiff(x,a,b):
    sum=0
    for j in range(len(a)):

        diff_sum=0

        for k in range(len(a)):
            if k==j:
                continue
            l_diff=1
            for i in range(len(a)):
                if j==i or i==k:
                    continue
                l_diff*= (x-a[i])/(a[j]-a[i])

            l_diff= l_diff/(a[j]-a[k])
            diff_sum+=l_diff
            
        sum+= b[j]*diff_sum


    return sum
    
    
    
    
    
    #simpsons 1/3 method
def int_simpson(f,a,b,n,x,y):
    if(n%2!=0):
        n+=1
    sum=(f(a,x,y)+f(b,x,y))
    h= (b-a)/n

    for i in range(1,n,2):
        sum+= 4*f(a+i*h,x,y) 
    
    for i in range(2,n,2):
        sum+= 2*f(a+i*h,x,y)

    intgn=sum*h/3

    return intgn


    
    
 


def Lagrand2F(x,a,b):
    h=0.01
    d1f= (-Lagrandiff(x+2*h,a,b) + 8*Lagrandiff(x+h,a,b) - 8*Lagrandiff(x-h,a,b) + Lagrandiff(x-2*h,a,b))/(12*h)
    return d1f


def Lagrand3F(x,a,b):
    h=0.01
    d2f= (-Lagrandiff(x+2*h,a,b) + 16*Lagrandiff(x+h,a,b) -30*Lagrandiff(x,a,b) + 16*Lagrandiff(x-h,a,b) - Lagrandiff(x-2*h,a,b))/(12*h**2)    
    return d2f
   
    
    
    
    
def Lagrancoeff(a,b):
    x_0 = f1(0,a,b)
    x_1 = Lagrandiff(0,a,b)

    x_2 = Lagrand2F(0,a,b)/2

    x_3 = Lagrand3F(0,a,b)/6

    return [x_0,x_1,x_2,x_3]    
    
    
