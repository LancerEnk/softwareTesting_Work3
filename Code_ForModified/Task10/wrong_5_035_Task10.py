# Task 10 : wrong_5_035
# 错误原因：算法出错，应该是if s[i]==s[i+1]。
# 修改方案：修改if s[i]==s[i-1]为if s[i]==s[i+1]。
def fun(input1,input2):
	n=int(input1)
	s = input2.lower()
	l=len(s)-1
	count=0
	for i in range(l):    # i的上界是len(s)-1且可取到此值
		if s[i]==s[i+1]:
			count+=1
	return(count)

# 输入时的代码段
# 输入格式：
# 第一行输入：4
# 第二行输入："RBBR"
input1=input()
input2=eval(input())
print(fun(input1,input2))
# wrong_5_035 end
