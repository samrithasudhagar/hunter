n=int(input())
l=list(map(int,input().split()))
k=""
s=""
for i in range(0,len(l)):
    if i==l[i]:
        k=k+str(i)+" "
k=sorted(k)
for i in k:
    s=s+str(i)+" "
print(s.strip())
