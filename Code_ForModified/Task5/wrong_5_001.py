# Task 5: wrong_5_001
def fun(input):
	a=input
	b=[] 
	c=(len(a)) 
	ret = ""
	for i in range(c):
		if a[i] =='a' or  a[i] =='A' or a[i] =='e' or  a[i] =='E' or a[i] =='i' or  a[i] =='I' or a[i] =='o' or  a[i] =='O' or a[i] =='u' or  a[i] =='u':
			continue
		else:
			k=ord(a[i]) 
			if k>64 and k<87:
				R=a[i].lower()
				b.append('.')
				b.append(R)
			else:
				b.append('.')
				b.append(a[i])
	for i in range(len(b)):
		#print(b[i],end="")
		ret += b[i]
	return ret
