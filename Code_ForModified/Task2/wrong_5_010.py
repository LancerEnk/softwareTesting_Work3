# Task 2: wrong_5_010
# 错误原因：思路整体出错
# 修改方式：重新写一份代码，重写的python代码见Right_Task2.py文件中
def fun(input):  
    n, m, a=map(int, input.split(" "))     
    surRect = n*m
    surFt = a*a
    needed = (surRect//surFt)     
    if surRect%surFt != 0:
        needed += surFt / (surRect%surFt*needed)
    return(needed)

# 获取输入数值时的代码段
imformation=input()
print(fun(imformation))
# wrong_5_010 end            
