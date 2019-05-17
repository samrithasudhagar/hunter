n=input()
s=list(n)
p=0
k=2
for i in range(len(n)):
    if i==0 and i==len(n)-1:
        p=p+int(s[i])**2
    elif i==len(n)-1:
       p=p+int(s[i])**1
    else:
        p=p+int(s[i])**k
    k=k+1
print(p)
