# Task 5: wrong_5_005
def fun(input):
	k = str(input)
	k = k.lower()
	s = ""
	L = ['a', 'e', 'i', 'o', 'u', 'y']

	for i in range(0, len(k)):
		if k[i] not in L:
			s += '-'
			s += k[i]
	return(s)
