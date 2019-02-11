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
 if k=="":
    print("-1")
 else:
    print(s.strip())
