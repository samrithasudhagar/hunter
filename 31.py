n=int(input())
l=list(map(int,input().split()))
m=0
p=1
for i in range(n-1):
    for j in range(i+1,n):
        p=1
        k=l[i:j+1]
        for o in k:
            p*=o
        if p>m:
            m=p
        
print(m)
