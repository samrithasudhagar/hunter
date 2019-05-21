n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    l.append(l[0])
    l.remove(l[0])
print(*l)
    
