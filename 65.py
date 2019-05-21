n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    if l[i]!=k:
        a.append(l[i])
if len(a)>0:
    print(*a)
else:
    print("empty")
    
