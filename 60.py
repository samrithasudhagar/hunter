n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(n):
    if m[0]==l[i]:
        print(i)
