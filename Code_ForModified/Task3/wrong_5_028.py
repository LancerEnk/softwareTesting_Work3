# Task 3: wrong_5_028
# 错误原因：if条件错误
# 修改方案：对if的条件进行修改，增加正数限制
def fun(input1,input2):
	n , k = map(int,input1.split())
	a=list(map(int,input2.split()))
	contestants=0
	for i in a:
		if i>=a[k-1] and i>0 :
			contestants+=1
	return(contestants)

#获取输入数值时的代码段
imformation1=input()
imformation2=input()
print(fun(imformation1,imformation2))
# wrong_5_028 end
