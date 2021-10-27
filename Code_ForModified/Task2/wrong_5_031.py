# id : wrong_5_031
def fun(input): 
    n,m,a = input.split()
    n,m,a = int(n),int(m),int(a)
    return(n*m//(a**2)+n*m%(a**2))
