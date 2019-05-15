n,k=map(int,input().split())
l=list(map(int,input().split()))
m=0
u=0
q=0
for i in range(len(l)):
	if l[i]>m:
		m=l[i]
while q<k-1:
	u=0
	for i in range(len(l)):
		if l[i]>u and l[i]<m:
			u=l[i]
			
	m=u
	q+=1
print(m)
