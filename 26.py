n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1,-1,-1):
    if i!=0:
        print(l[i],end="->")
    else:
        print(l[i])
