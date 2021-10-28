# Task 5: wrong_5_031
def fun(input):
	ret = ""
	n=input
	s=[]
	for i in range(len(n)):
		 if n[i]=='A' or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U' or n[i]=='Y' or n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u' or n[i]=='y':
			  pass
		 else:
			  s.append(n[i])
	for i in range(len(s)):
		 if i%2==0:
			  s.append('.')
	for i in range(len(s)):
		 ret+=(s[i])
	return ret
