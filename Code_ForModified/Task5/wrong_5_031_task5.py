# Task 5: wrong_5_031
# 错误原因：
# 	问题1：没有对字母的大小写进行处理。
# 	问题2：加 ‘.’ 的计算方法有误。
# 修改方案：
# 	问题1：在向s中append(n[i])时直接用lower()方法加入小写字母进去，不论该字母原来是大写还是小写。
# 	问题2：在向s中append(n[i])前先append(‘.’)，与此同时删去原本的append(‘.’)部分代码。
def fun(input):
	ret = ""
	n=input
	s=[]
	for i in range(len(n)):
		 if n[i]=='A' or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U' or n[i]=='Y' or n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u' or n[i]=='y':
			  pass
		 else:
			  s.append('.')
			  s.append(n[i].lower())
	for i in range(len(s)):
		 ret+=(s[i])
	return ret

# 获取输入数值时的代码段
str1=input()
print(fun(str1))
# wrong_5_031 end
