# Task 5: wrong_5_001
# 错误原因：原第8行，现第10行的if条件出错，在判断时将a[i]=='U'的条件写成a[i]=='u'，后者重复两次，而且没有加入Y和y的判定。
# 修改方案：修改现第10行的if条件。
def fun(input):
	a=input
	b=[] 
	c=(len(a)) 
	ret = ""
	for i in range(c):
		if a[i] =='a' or  a[i] =='A' or a[i] =='e' or  a[i] =='E' or a[i] =='i' or  a[i] =='I' or a[i] =='o' or  a[i] =='O' or a[i] =='u' or  a[i] =='U' or a[i] =='y' or a[i] =='Y':
			continue
		else:
			k=ord(a[i]) 
			if k>64 and k<87:
				R=a[i].lower()
				b.append('.')
				b.append(R)
			else:
				b.append('.')
				b.append(a[i])
	for i in range(len(b)):
		#print(b[i],end="")
		ret += b[i]
	return ret

# 获取输入数值时的代码段
str1=input()
print(fun(str1))
