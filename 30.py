n=int(input())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
c=1
k=f[0]
for i in range(1,n):
    if s[i]>=k:
        c=c+1
    k=s[i]
print(c)
