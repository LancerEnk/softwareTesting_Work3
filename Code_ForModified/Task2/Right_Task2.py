# 自写的Task2 python版正确代码：
# 用于对wrong_5_010.py、wrong_5_031.py的整体修改
import math
def fun(input):
    n,m,a=list(map(int,input.split()))
    x=math.ceil(m/a)
    y=math.ceil(n/a)
    return(x*y)

imformation=input()
print(fun(imformation))
# Task 2 end
