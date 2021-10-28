# Task 9: wrong_5_032  
# 错误原因：使用replace()函数对首字母进行处理时，只是将替换后的首字母赋给了b，但没有给b增加非首字母的字符串，因此应该在后续为b补上a的后续字母。
# 修改方法：为b赋予a的后续字符串，使用python中string的截取方法。
def fun(input):
	a = input 
	if a[0].isupper() == True:
		return(a)
	elif a[0].isupper() == False:
		b = a[0].replace(a[0],a[0].upper(),1)
		b+=a[1:]
		return(b)
	
# 获取输入数值时的代码段
# 输入格式："konjac"
str1=eval(input())
print(fun(str1))
# wrong_5_032 end
