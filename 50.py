n,k=map(int,input().split())
c=0
if k>n:
    print(0)
else:
    while n>0:
        n=n-k
        c=c+1
    if n==0:
        print(c)
 #i
