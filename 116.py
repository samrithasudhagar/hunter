s,a=map(str,input().split())
p=[]
q=[]
ans=[]
if len(s)<len(a):
    k=len(a)-len(s)
    for i in range(len(s)):
        p.append(s[i])
    for i in range(len(a)):
        q.append(a[i])
else:
    k=len(s)-len(a)
    for i in range(len(a)):
        p.append(a[i])
    for i in range(len(s)):
        q.append(s[i])
for i in range(1,k+1):
    p.append(i)

if len(s)<len(a):
    for i in range(len(p)):
        ans.append(p[i])
        ans.append(q[i])
else:
    for i in range(len(p)):
        ans.append(q[i])
        ans.append(p[i])
for i in range(len(ans)):
    print(ans[i],end="")

        
