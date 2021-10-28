def fun(input1,input2):
	n,k=map(int,input1.split())
	x=list(map(int,input2.split()))
	r=0
	for i in range(len(x)):
		if x[i]>0 and x[i]>i and x[i]>=k:
			r+=1
	return(r)
