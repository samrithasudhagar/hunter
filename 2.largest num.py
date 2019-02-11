n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
k=[]
s=""
for i in range(0,len(l)):
        k.append(l[-1])
        l.remove(l[-1])
if sum(l)==0:
    print("0")
else:
    for i in k:
         s=s+str(i)
    print(s)

