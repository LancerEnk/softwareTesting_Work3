# Task 1:
# 错误原因：2不能被划分为两偶数之和，因此需要特殊考虑Weight==2的情况。
def fun(Weight):
    if (Weight % 2 == 0 and Weight != 2):
        return("YES")
    else:
        return("NO")

# 获取输入数值时的代码段：
w=int(input())
print(fun(w))
# Task 1 end
