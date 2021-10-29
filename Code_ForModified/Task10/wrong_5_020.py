# Task 10 : wrong_5_020
def fun(input1,input2):
	ret+=""
	stones = int(input1)
	colors = str(input2).upper()
	colors_list = ['R', 'G', 'B']
	for c in colors:
		if c not in colors_list:
			ret+=(c)
		else:
			continue 
	if stones > 50:
		ret+=(stones) 
	if len(colors) != stones:
		ret+=(len(colors)) 
	ret+=("stones: colors: "+stones, colors) 
	count = 0
	for i in range(len(colors) -1):
		if colors[i] == colors[i+1]:
			count += 1
		else:
			continue        
	ret+=("minimum stones: "+count)
	return ret
