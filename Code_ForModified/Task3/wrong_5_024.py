# Task 3: wrong_5_024
# 错误原因：题干要求只有分数为正的才能进入下一轮，但在文件中的if代码段中没有非零的限制。
# 修改方案：对if的条件进行修改，增加正数限制
def fun(input1,input2):
	n,k = map(int,input1.split())
	scores = list(map(int,input2.split()))
	flag = 0
	for i in scores:
		if i >= scores[k-1] and i>0 :
			flag += 1
	return(flag)
 
#获取输入数值时的代码段
imformation1=input()
imformation2=input()
print(fun(imformation1,imformation2))
