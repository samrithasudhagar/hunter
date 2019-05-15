n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if sum(l[:i])==sum(l[i+1:]):
        c=c+1
if c>0:
    print("yes")
else:
    print("no")
