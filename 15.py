n=int(input())
l=list(map(int,input().split()))
s=[]
r=[]
for i in range(1,len(l)-1):
	if l[i]>l[i+1]:
		if l[i]>l[i-1]:
			s.append(l[i])
			r.append(l[i])
		else:
			r.append(l[i])
r.append(l[-1])
if l[-1]>l[-2]:
	s.append(l[-1])

print(*r)
print(*s)
