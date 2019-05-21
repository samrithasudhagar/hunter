n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        s.append(l[i+1])
    elif l[i]<=l[i+1]:
        s.append(-1)
    if i+1==len(l)-1:
        s.append(-1)
print(*s)    
