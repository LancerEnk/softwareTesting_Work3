# Task 5: wrong_5_005
# 错误原因：原第10行、现第12行的 s += '-' 出错，题干中的衔接是用'.'进行的，应该用 s += '.'
# 修改方案：将 s += '-' 改为 s += '.'
def fun(input):
	k = str(input)
	k = k.lower()
	s = ""
	L = ['a', 'e', 'i', 'o', 'u', 'y']

	for i in range(0, len(k)):
		if k[i] not in L:
			s += '.'
			s += k[i]
	return(s)

# 获取输入数值时的代码段
str1=input()
print(fun(str1))
# wrong_5_005 end
