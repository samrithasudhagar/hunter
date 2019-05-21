n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
    if i==len(l)-1:
        s.append(0)
    else:
        k=max(l[i+1:])
        s.append(k)
print(*s)
