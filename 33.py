s=input()
c=1
f=1
m=0
for i in range(0,len(s)-1):
    if f==0 and (s[i]=="a" and s[i+1]=="b" or s[i]=="b" and s[i+1]=="a"):
        
        c=c+1
        if c>m:
            m=c
    elif (s[i]=="a" and s[i+1]=="a" or s[i]=="b" and s[i+1]=="b") and f==0:
      
    
      
        c=1
        f=1
    elif f==1 and (s[i]=="a" and s[i+1]=="b"):
       
        c=c+1
        if c>m:
            m=c
        f=0
    elif f==1 and (s[i]=="b" and s[i+1]=="a"):
        c=1
        f=1
print(m)
