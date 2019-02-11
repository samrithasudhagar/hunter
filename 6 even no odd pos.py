n=int(input())
l=list(map(int,input().split()))
s=""
for i in range(0,len(l)):
    if (l[i]%2==0 and i%2==1) or (l[i]%2==1 and i%2==0):
        s=s+str(l[i])+" "
print(s.strip())
