n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1,n):
        if l[i]+l[j]==k:
            c=0
            break
        else:
            c=1
    if c==0:
        break
if c==0:
    print("YES")
else:
    print("NO")
