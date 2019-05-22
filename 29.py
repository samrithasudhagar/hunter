n=int(input())
l=list(map(int,input().split()))
m=-10000
for i in range(n-1):
    for j in range(i+1,n+1):
        if sum(l[i:j])>m:
            m=sum(l[i:j])
print(m)
