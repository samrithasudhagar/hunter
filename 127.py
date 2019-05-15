s,a=map(str,input().split())
m=""
for j in range(len(a)):
    for i in range(len(a)-1,-1,-1):
        if a[j:i+1] in s:
            if len(a[j:i+1])>len(m):
                m=a[j:i+1]
print(m)
        
        
