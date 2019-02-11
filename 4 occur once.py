n=int(input())
l=list(map(int,input().split()))
k=""
for i in l:
    if l.count(i)==1:
        k=k+str(i)
print(k)
