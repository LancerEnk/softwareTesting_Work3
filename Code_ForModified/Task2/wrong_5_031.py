# id : wrong_5_031
# 错误原因：思路整体出错
# 修改方式：重新写一份代码，重写的python代码见Right_Task2.py文件中
def fun(input): 
    n,m,a = input.split()
    n,m,a = int(n),int(m),int(a)
    return(n*m//(a**2)+n*m%(a**2))

# 获取输入数值时的代码段
imformation=input()
print(fun(imformation))
# wrong_5_031 end       
