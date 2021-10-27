# id : wrong_5_043 
def fun(input):  
    n,m,a = input.split() 
    n=int(n)
    m=int(m)
    a=int(a)
    if(n<=a and m<=a):
        return('1')
    else:
        if(n%a==0):
            x = n//a
            if(m%a==0):
                y=m//a
                return(x+y-1)
            else:
                y=m//a + 1
                return(x+y)
        else:
            x= n//a +1
            if(m%a==0):
                y=m//a
                return(x+y)
            else:
                y= m//a +1
                return(x+y)
