n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n+1):
    if i*n in l:
        c=c+1
print(c)
