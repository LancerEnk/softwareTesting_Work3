# id : wrong_5_017
def fun(input):
	lst = []
	x = y = 0
	for i in range(5):
		matrix = input[i].split()
		lst.append(matrix)
	for j in range(5):
		if lst[i][j] == '1':
			x = i-2
			y = j-2
	return(abs(x) + abs(y))
