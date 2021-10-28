# Task 4 : wrong_5_040
# 错误原因：返回值return的计算方式错误
# 修改方法：修改return中的表达式
import math
def fun(input):
    n,m = map(int,input.split())
    return((n*m)//2)

# 获取输入数值时的代码段
str1=input()
print(fun(str1))
# wrong_5_040 end
