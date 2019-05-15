n=int(input())
l=list(map(int,input().split()))
l.sort()
k=[]
while len(l)>0:
    k.append(l[-1])
    l.remove(l[-1])
    if len(l)>0:
        k.append(l[0])
        l.remove(l[0])
print(*k)
    
