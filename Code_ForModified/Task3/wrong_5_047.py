# Task 3: wrong_5_047
# 错误原因：if条件出错；i的范围是0~len(a)-1，这是数组的限制所导致的，因此在算人数时应该c=i+1
# 修改方案：对if的条件进行修改，增加正数限制
def fun(input1,input2):
	n,k=map(int,input1.split())
	a=[int(x) for x in input2.split()]
	c=0
	for i in range(0,len(a)):
		if a[i]>=a[k-1] and a[i]>0 :
			c=i+1 
	return(c)

# 获取输入数值时的代码段
imformation1=input()
imformation2=input()
print(fun(imformation1,imformation2))
# wrong_5_047 end 
