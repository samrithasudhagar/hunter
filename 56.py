n=int(input())
l=list(map(int,input().split()))
m=100000
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if abs(l[i]+l[j])<m:
            m=abs(l[i]+l[j])
            a=l[i]
            b=l[j]
if a>b:
    print(a,b)
else:
    print(b,a)
    
