n=int(input())
l=list(map(int,input().split()))
u,v=map(int,input().split())
m=1000000
k=-1
p=-1
for i in range(0,n):
    if l[i]==u:
        k=i
    if l[i]==v:
        p=i
    if k!=-1 and p!=-1:
        if abs(k-p)<m:
            m=abs(k-p)
print(m)
        
