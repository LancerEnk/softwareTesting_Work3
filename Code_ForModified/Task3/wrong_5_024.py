# Task 3: wrong_5_024
def fun(input1,input2):
	n,k = map(int,input1.split())
	scores = list(map(int,input2.split()))
	flag = 0
	for i in scores:
		if i >= scores[k-1]:
			flag += 1
	return(flag)
