n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
for i in range(len(l)):
    if i!=len(l)-1:
        print(l[i],end="->")
    else:
        print(l[i])
