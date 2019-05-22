n,k=map(int,input().split())
if k>n:
    print(0)
c=0
while n>0:
    n=n-k
    c=c+1
if n==0:
    print(c)
