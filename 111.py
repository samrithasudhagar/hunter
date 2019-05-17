n=int(input())
k=[]
s=0
for i in range(n):
    l=list(map(int,input().split()))
    k.append(l)
for i in range(n):
    for j in range(n):
        if i==j:
            s=s+k[i][j]
print(s)
#i
