n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(l[i]+m[i])
print(*a)   
