n=int(input())
l=list(map(int,input().split()))
max=l[0]
min=l[0]
for i in range(n):
    if l[i]>max:
        max=l[i]
    if l[i]<min:
        min=l[i]
print(max-min)
