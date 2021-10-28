# Task 5: wrong_5_018
def fun(input):
	l=input
	j=list(l)
	k=[]
	n=["a","e","i","o","u","A","E","O","I","U"]
	h=0
	for i in l:
		try:
			if i in n :
				del j[j.index(i)]
			else:
				if i.isupper():
					j.insert(j.index(i),".")
					#j[j.index(i)]=j[j.index(i)].lower()
					h=h+1
					k.append(j.index(i)+h-1)
				else:
					j.insert(j.index(i),".")
					h=h+1
		except:
			pass
	for i in k:
		j[i]=j[i].lower()
	return("".join(j))
