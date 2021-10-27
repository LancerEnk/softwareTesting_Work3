# id : wrong_5_048 
# 错误原因1：a*a>=n*m时只意味正方形的总面积大于待铺砖的长方形，但不意味着能够铺满。大正方形砖虽然面积大，但无法覆盖长方形广场，长方形广场虽然长但是扁，根本不能被大正方形砖所遮盖”的情况。
# 错误原因2：在(a<n and a<m)的分支中，y的计算方法有误，return的值应为x*y
# 修改方法：对代码段的if判断语句进行修改
# 以下是修改的最少代码段的修改方式：只在原语句上进行修改，没有整体删除语句的情况发生
import math
def fun(input):
    n,m,a=list(map(int,input.split()))
    if (a>=m and a>=n):
        return(1)
    elif a>=m :
        return(math.ceil(n/a))
    elif a>=n :
        return(math.ceil(m/a))
    else:
        x=math.ceil(m/a)
        y=math.ceil(n/a)
        return(x*y)

# 获取输入数值时的代码段      
imformation=input()
print(fun(imformation))
# wrong_5_048 end
