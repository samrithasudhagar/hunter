n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    k.append(l.count(l[i]))
for i in range(len(k)):
    ss=max(k)
    if ss==k[i]:
        print(l[i])
        break
        
