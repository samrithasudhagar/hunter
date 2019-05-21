l=list(map(str,input().split()))
s=[]
for i in range(len(l)-1,-1,-1):
	s.append(l[i])
print(*s)
