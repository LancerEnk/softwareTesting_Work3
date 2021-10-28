# id : wrong_5_003
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
	return(abs(x+y-4))
