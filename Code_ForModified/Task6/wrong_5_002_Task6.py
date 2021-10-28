# id : wrong_5_002
# 错误原因：在现第10行进行遍历时，使用range(len(a)-1)，这实际给i取的是 0 <= i <= len(a)-2 的值，不能够使i遍历到a[i]和b[i]的最后一位。
# 修改方案：将range(len(a)-1)改成range(len(a))
def fun(input1,input2):
	a = str(input1).lower()
	b = str(input2).lower()
	if a == b:
		return("0")
	else:
		for i in range((len(a)-1)):
			if (a[i] < b[i]):
				return("-1")            
			if (a[i] > b[i]):
				return("1")

# 获取输入数值时的代码段
str1=input()
str2=input()
print(fun(str1,str2))
# wrong_5_002 end
