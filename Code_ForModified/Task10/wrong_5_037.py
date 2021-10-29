# Task 10 : wrong_5_037
def fun(input1,input2):
	n = int(input1)
	lst = list(map(str,input2.split()))[:n]
	left = 0
	right = len(lst) - 1
	count = 0
	for i in range(len(lst)) :
		if left < right:
			if lst[left] == lst[left + 1]:
				count += 1
		left += 1
	return (count) 
