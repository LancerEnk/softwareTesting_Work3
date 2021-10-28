# id : wrong_5_017
# 错误原因：本代码逻辑为for i in range(5)后接for j in range(5)，二者是顺序关系。
#          因此在进行第二个for循环时默认i=4，此时如果输入的用例在最后一行有1，即能搜到对应的j使lst[i][j] == '1'，否则搜不到对应的i和j，则导致答案出错。
# 修改方案：给第二个for循环外层嵌套一个关于i的从0~4的循环。
def fun(input):
	lst = []
	x = y = 0
	for i in range(5):
		matrix = input[i].split()
		lst.append(matrix)
	for i in range(5):
		for j in range(5):
			if lst[i][j] == '1':
				x = i-2
				y = j-2
	return(abs(x) + abs(y))

# 获取输入数值时的代码段
# 输入格式为：["0 0 0 0 0","0 0 0 0 0","0 1 0 0 0","0 0 0 0 0","0 0 0 0 0"]
str1=eval(input())
print(fun(str1))
# wrong_5_017 end
