n,k=map(int,input().split())
l=list(map(int,input().split()))
v=[]
l.remove(k)
for i in range(len(l)):
	v.append([l[i],abs(l[i]-k)])
v.sort(key=lambda x:x[1])
for i in range(3):
	print(v[i][0],end=" ")
	
