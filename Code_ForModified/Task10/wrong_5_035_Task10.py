# Task 10 : wrong_5_035
def fun(input1,input2):
	n=int(input1)
	s = input2.lower()
	l=len(s)-1
	count=0
	for i in range(l):
		if s[i]==s[i-1]:
			count+=1
	return(count)
