n=int(input())
l=list(map(str,input().split()))
k=input()
p=len(k)
c=0
for i in l:
        if i[:p]==k:
            c=c+1
print(c)
