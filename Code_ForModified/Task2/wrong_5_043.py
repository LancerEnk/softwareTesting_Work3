# id : wrong_5_043 
# 错误原因：在计算时，获取到的x和y代表在长、宽上各应用到多少个a*a的正方形，因此在return结果时应该return(x*y)，而不应该对x和y进行相加操作
# 修改方式：修改return的值即可
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
                return(x*y)
            else:
                y=m//a + 1
                return(x*y)
        else:
            x= n//a +1
            if(m%a==0):
                y=m//a
                return(x*y)
            else:
                y= m//a +1
                return(x*y)

# 获取输入数值时的代码段            
imformation=input()
print(fun(imformation))
# wrong_5_043 end
