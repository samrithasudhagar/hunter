n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ii=[]
for i in range(n):
    for j in range(k):
        if l[i][j]==0:
            ii.append([i,j])
for i in range(len(ii)):
    for j in range(2):
        if j==0:
            u=ii[i][j]
            for p in range(k):
                l[u][p]=0
        if j==1:
            t=ii[i][j]
            for q in range(n):
                l[q][t]=0
for i in range(len(l)):
    print(*l[i])
