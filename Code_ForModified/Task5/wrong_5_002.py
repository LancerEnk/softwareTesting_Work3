# Task 5: wrong_5_002
def fun(input):
    n=input.lower()
    res=''
    for i in range(len(n)):
        if(n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'):
            continue
        else:
            res=res+n[i]
    k='.'
    for i in range(len(res)):
        m='.'
        if(i==0):
            k=k+res[i]
        else:
            k=k+m+res[i]
    return(k)
