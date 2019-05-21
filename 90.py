s=input()
c=0
k=s[0]
m=0
hi=""
for i in range(len(s)-1):
    if s[i]==k:
        c=c+1
    if s[i]!=s[i+1]:
        if c>m:
            m=c
            hi=s[i]
        c=0
        k=s[i+1]
    if i+1==len(s)-1 :
        if c+1>m:
            m=c+1
            hi=s[i]
        
print(hi,end=" ")
print(m,end="")
