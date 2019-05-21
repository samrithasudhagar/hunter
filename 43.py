s=input()
a=[]
m=0
n=""
for i in range(len(s)-1):
    if s[i].isdigit() and s[i+1].isdigit():
        n=s[i]+s[i+1]
        if int(n)%2==0:
            a.append(int(n)*s[i-1])
        else:
            a.append(s[i-1])
            a.append(n)
    elif s[i].isdigit() and s[i+1].isdigit()==False:
        
        if int(s[i])%2==0:
            a.append(int(s[i])*s[i-1])
        else:
            a.append(s[i-1])
            a.append(s[i])
    elif s[i+1].isdigit() and s[i].isdigit()==False and i+1==len(s)-1:
        if int(s[i+1])%2==0:
            a.append(int(s[i+1])*s[i])
        else:
            a.append(s[i])
            a.append(s[i+1])
        
            
for i in a:
    print(i,end="")
            
