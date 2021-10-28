# id : wrong_5_002
def fun(input1,input2):
	a = str(input1).lower()
	b = str(input2).lower()
	if a == b:
		return("0")
	else:
		for i in range((len(a)-1)):
			if (a[i] < b[i]):
				return("-1")            
			if (a[i] > b[i]):
				return("1")
