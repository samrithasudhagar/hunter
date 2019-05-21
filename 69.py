s=input()
m=s.count("@")
l=s.count(".")
for i in range(len(s)):
    if s[i]=="@":
        n=i
        q=s[:i]
       
    if s[i]==".":
        k=i
       
if m==1 and l==1 and k-n<=5 and len(q)>=3 and s[len(s)-4:]==".com":
    print("YES")
else:
    print("NO")
 
