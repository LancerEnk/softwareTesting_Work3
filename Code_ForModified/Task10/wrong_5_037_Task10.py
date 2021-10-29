# Task 10 : wrong_5_037
# 错误原因：在代码段“lst = list(map(str,input2.split()))[:n]”中，
#          通过print(lst)发现，此步中存储的lst在输出后是“['RRG']”，这说明在存储时并没有挨个字母存进去，
#          而是把所有的字母压缩成为了一个字符串存进了list中。
#          因此这一步导致后续代码出现wrong answer，使无论什么输入，代码的输出都是0。
# 修改方案：将input2的接收方式进行修改，改为lst = list(input2.upper())。
def fun(input1,input2):
	n = int(input1)
	lst = list(input2.upper())
	#print(lst)
	left = 0
	right = len(lst) - 1
	count = 0
	for i in range(len(lst)) :
		if left < right:
			if lst[left] == lst[left + 1]:
				count += 1
		left += 1
	return (count) 

# 输入时的代码段
# 输入格式：
# 第一行输入：4
# 第二行输入："RBBR"
input1=input()
input2=eval(input())
print(fun(input1,input2))
# wrong_5_037 end
