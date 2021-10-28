# id : wrong_5_003
# 错误原因：在最终return的返回值计算过程中，应该给(x-2)和(y-2)分别取绝对值，不应该取abs((x-2)+(y-2))。
# 修改方案：修改return (abs(x+y-4))为return(abs(x-2)+abs(y-2))。
def fun(input):
	ar=[]
	x=0
	y=0
	for i in range(5):
		x=list(map(int,input[i].split()))
		ar.append(x)

	for i in range(5):
		for j in range(5):
			if ar[i][j]==1:
				x=i
				y=j
				break
	return(abs(x-2)+abs(y-2))

# 获取输入数值时的代码段
# 输入格式为：["0 0 0 0 0","0 0 0 0 0","0 1 0 0 0","0 0 0 0 0","0 0 0 0 0"]
str1=eval(input())
print(fun(str1))
# wrong_5_003 end
