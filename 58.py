n,k=map(int,input().split())
c=0
l=list(map(int,input().split()))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if abs(l[i]-l[j])==k:
            c=c+1
print(c) 
