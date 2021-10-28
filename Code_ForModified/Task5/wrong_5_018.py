# Task 5: wrong_5_018
# 错误原因：
# 	问题1：在删除元音时漏删除y和Y。
# 	问题2：字母转换大小写时，应该将j.index(i)位加入K中进行处理，这意味着要处理的是字母i，不应该在后面加与h相关的编号。
# 	问题3：在给j插入”.”时，应该通过h相关编号来加（因为h是自增的），而与当前字母i在第几位没关系，只需要留h相关的代数式就行。
# 	问题4：每次h的自增应该自增2，因为不仅要跳过当前字母，还要跳过加入的”.”，即一共要跳过两个位置编号。
# 	问题5：将大写字母存进K中，在最后对K遍历处理时，只会对j中的第一个重复大写字母进行处理（如TTT只会处理为tTT），无法全部变小写。
# 解决方案：
# 	问题1：补充n数组。
# 	问题2：将现第29行改为：k.append(j.index(i))。
# 	问题3：将现第26行和现第31行改为：j.insert(h,".")。
# 	问题4：将所有的h=h+1都改为h=h+2。
# 	问题5：不遍历K数组，改为遍历j数组，虽然这样一来代码执行效率变低，但是可以让所有大写字母都被遍历到，从而修改为小写字母。
def fun(input):
	l=input
	j=list(l)
	k=[]
	n=["a","e","i","o","u","A","E","O","I","U","y","Y"]
	h=0
	for i in l:
		try:
			if i in n :
				del j[j.index(i)]
			else:
				if i.isupper():
					j.insert(h,".")
					#j[j.index(i)]=j[j.index(i)].lower()
					h=h+2
					k.append(j.index(i))
				else:
					j.insert(h,".")
					h=h+2
		except:
			pass
	for i in j:
		j[j.index(i)]=j[j.index(i)].lower()
	return("".join(j))

# 获取输入数值时的代码段
str1=input()
print(fun(str1))
# wrong_5_018 end
