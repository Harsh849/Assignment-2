# this is function for root finding

def NR_rt(F,f,x_s,x_t,x,y):
    while abs(F(x_s,x,y))>x_t:
        x_s =x_s - F(x_s,x,y)/f(x_s,x,y)
    return x_s



def NR1_rt(F,f,x_s,x_t,x,y,p,q):
    while abs(F(x_s,x,y,p,q))>x_t:
        x_s =x_s - F(x_s,x,y,p,q)/f(x_s,x,y,p,q)
    return x_s
