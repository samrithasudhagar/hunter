s,k=map(str,input().split())
k=int(k)
a=[]
for i in range(len(s)):
    if len(s[i:i+k])==k:
        a.append(s[i:i+k])
print(*a)
#i
