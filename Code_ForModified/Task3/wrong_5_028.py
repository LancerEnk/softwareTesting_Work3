# Task 3: wrong_5_028
def fun(input1,input2):
	n , k = map(int,input1.split())
	a=list(map(int,input2.split()))
	contestants=0
	for i in a:
		if i > k:
			contestants+=1
	return(contestants)
