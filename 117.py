s=input()
l=list(s)
p=0
k=0
for i in range(len(s)):
    p=p+(int(l[i])**k)
    k=k+1
print(p)
