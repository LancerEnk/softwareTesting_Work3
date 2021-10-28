# id : wrong_5_032  
def fun(input):
	a = input 
	if a[0].isupper() == True:
		return(a)
	elif a[0].isupper() == False:
		b = a[0].replace(a[0],a[0].upper(),1)
		return(b)
