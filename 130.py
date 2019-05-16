n=int(input())
c=0
s=[]
for i in range(3,n+1):
	for j in range(2,i):
		if j%i==0:
			c=1
			break
	if c==0:
		if i%10==3:
			s.append(i)
print(sum(s))
	
