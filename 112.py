n=int(input())
a=0
b=1
d=0
cl=0
for i in range(n):
    c=a+b
    d=0+c
    if d==n:
        cl=1
        break
    b=c
    a=c
if cl==1:
    print("YES")
else:
    print("NO")
