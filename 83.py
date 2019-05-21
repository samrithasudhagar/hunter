s=input()
k=""
m=0
for i in range(len(s)-1):
    k=""
    if s[i]==s[i+1]:
        k=k+s[:i+1]+s[i+2:]
        if int(k)>m:
            m=int(k)
print(m)
