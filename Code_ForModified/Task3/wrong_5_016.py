# Task 2: wrong_5_016
# 错误原因：if判断语句出错，本题的判断方式应该是(x[i]>0) and (x[i]>=x[k-1])时，通过的人数r++。
# 修改方式：修改if语句
def fun(input1,input2):
	n,k=map(int,input1.split())
	x=list(map(int,input2.split()))
	r=0
	for i in range(len(x)):
		if x[i]>0 and x[i]>=x[k-1]:
			r+=1
	return(r)

# 获取输入数值时的代码段
imformation1=input()
imformation2=input()
print(fun(imformation1,imformation2))
# wrong_5_016 end
