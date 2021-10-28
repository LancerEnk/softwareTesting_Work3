# id : wrong_5_041
# 错误原因：在第11行有return n，这意味着程序进行到此步将直接结束运行，不会再进行下面第12行~20行的步骤，即数字之间不会再＋“+”。
# 修改方案：注释/删除这行return n。
def fun(input):
	a=input
	l=len(a)
	i=0
	n=[]
	while i<l:
		n.append(int(a[i]))    
		i=i+2    
	n.sort()
	# return n
	m=""
	for x in range(0,len(n)):
		s=str(n[x])
		if x==len(n)-1:
			m=m+s
		else:   
			s=str(n[x])  
			m=m+s+"+"        
	return m

# 获取输入数值时的代码段
# 输入格式为："1+2+1+2+2+2+2+1+3+3"
str1=eval(input())
print(fun(str1))
# wrong_5_017 end
