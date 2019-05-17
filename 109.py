n=int(input())
l=[]
s=list(map(str,input().split()))
for i in s:
    l.append(i.lower())
k=sorted(l)
for i in range(len(k)):
    print(k[i])
