def prime(n):
    cl=0
    if n==2:
        return 1
    elif n==1:
        return 0
    else:
        for i in range(2,n):
            if n%i==0:
                cl=1
                break
            else:
                cl=0
        if cl==0:
            return 1
        else:
            return 0
n=int(input())
c=[]
for i in range(n+1):
    for j in range(n+1):
        if i+j==n:
            if prime(i)==1 and prime(j)==1:
                if i not in c and j not in c:
                    c.append(i)
                    c.append(j)
                
print(len(c)//2)
    
