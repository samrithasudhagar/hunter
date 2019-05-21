n=int(input())
l=list(map(int,input().split()))
a=[l[0]]
for i in range(1,len(l)):
    a.append(min(l[:i+1]))
print(*a)
