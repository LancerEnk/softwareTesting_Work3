# id : wrong_5_041
def fun(input):
	a=input
	l=len(a)
	i=0
	n=[]
	while i<l:
		n.append(int(a[i]))    
		i=i+2    
	n.sort()
	return n
	m=""
	for x in range(0,len(n)):
		s=str(n[x])
		if x==len(n)-1:
			m=m+s
		else:   
			s=str(n[x])  
			m=m+s+"+"        
	return m
