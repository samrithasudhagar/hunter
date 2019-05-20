n=int(input())
k=list(map(int,input().split()))
s=1
v=[]
for i in range(len(k)):
    s=1
    for j in range(len(k)):
        if j!=i:
            s=s*k[j]
    v.append(s)
print(*v)
        
