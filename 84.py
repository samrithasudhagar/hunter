s=input()
c=0
m=0
k=s[0]
l=""
for j in range(len(s)-1):
    if s[j]==k:
        c=c+1
        if c>m:
            m=c
    if s[j]==s[j+1] and j+1==len(s)-1:
        l=l+(str(m+1))+"*"+s[j]
    if s[j]!=s[j+1] and j+1==len(s)-1 and m>1:
        l=l+str(m)+"*"+s[j]+s[j+1]
    if s[j]!=s[j+1] and j+1==len(s)-1 and m==1:
        l=l+s[j]+s[j+1]
            
    
    if s[j+1]!=s[j] and j+1!=len(s)-1:
        if m>1:
            l=l+str(m)+"*"+s[j]
            k=s[j+1]
            c=0
            m=0
        
        else:
            l=l+s[j]
            k=s[j+1]
            c=0
            m=0

print(l)      
