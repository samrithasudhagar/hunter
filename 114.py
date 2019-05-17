def sumofdig(n):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return(s)
a=[]
bl=0
l,r=map(int,input().split())
for i in range(l,r+1):
        k=sumofdig(i)
        
        if k==2:
            a.append(i)
        else:
            for j in range(2,k):
                if k==1:
                    bl=1
                else:
                    if k%j==0:
                        bl=1
                        break
                    else:
                        bl=0
            if bl==0 and k!=1:
                a.append(i)
print(len(a))
                
