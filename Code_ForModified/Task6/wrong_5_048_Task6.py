# id : wrong_5_048
def fun(input1,input2):
	ret ="";
	n = len(input1)
	for i in range(n):
		if input1[i].lower() == input2[i].lower():
			pass
		elif input1[i].lower() < input2[i].lower():
			ret+=("-1")            
		elif input1[i].lower() > input2[i].lower():
			ret+=("1")            
	ret+=("0")
	return ret
