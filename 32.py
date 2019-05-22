n=int(input())
l=list(map(int,input().split()))
a=l
k=[]
while len(a)>1:
    for i in range(len(a)):
        if i%2!=0:
            k.append(a[i])
    a=k
    k=[]
if len(a)==1:
    print(l.index(a[0]))
