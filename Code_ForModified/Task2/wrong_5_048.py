# id : wrong_5_048 
import math
def fun(input):
    n,m,a=list(map(int,input.split()))
    if a*a >= n*m:
        return(1)
    elif a>=m :
        return(math.ceil(n/a))
    elif a>=n :
        return(math.ceil(m/a))
    else:
        x=math.ceil(m/a)
        y=math.ceil((n-a)/a)
        return(x*y*x)
