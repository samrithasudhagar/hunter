n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l2:
    if i in l1:
        flag=0
    else:
        flag=1
        break
if flag==0:
    print("YES")
else:
    print("NO")
