n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]<a[j] and i<j:
            c=c+1
print(c)
