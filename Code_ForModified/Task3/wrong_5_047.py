# Task 3: wrong_5_047
def fun(input1,input2):
	n,k=map(int,input1.split())
	a=[int(x) for x in input2.split()]
	c=0
	for i in range(0,len(a)):
		if a[i]==k:
			c=i-1 
	return(c)
