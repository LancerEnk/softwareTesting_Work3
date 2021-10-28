# id : wrong_5_048
# 错误原因：
#	问题1：在所有的涉及到对ret进行改动的代码时，不应该给ret+=“1”、“-1”、“0”，而应该直接设置ret的字符值为“1”、“-1”、“0”。
#	问题2：在str1和str2出现第一个不同的字母时，就已经完成结果的比较了，因此如果进入到input1[i].lower() != input2[i].lower()的分支中，
#	      给ret赋完值以后应该直接return结果，不应该再接着比较下去。
# 修改方案：
#	问题1：将所有的ret+=“1”、“-1”、“0”改成ret=“1”、“-1”、“0”。
#	问题2：在两个elif分支的末尾加上return ret。
def fun(input1,input2):
	ret ="";
	n = len(input1)
	for i in range(n):
		if input1[i].lower() == input2[i].lower():
			pass
		elif input1[i].lower() < input2[i].lower():
			ret=("-1")
			return ret
		elif input1[i].lower() > input2[i].lower():
			ret=("1") 
			return ret
	ret=("0")
	return ret

# 获取输入数值时的代码段
str1=input()
str2=input()
print(fun(str1,str2))
# wrong_5_048 end
