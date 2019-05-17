def prime(n):
    c=0
    if n==2:
        return 1
    elif n==1:
        return 0
    else:
        for i in range(2,n):
            if n%i==0:
                c=1
                break
            else:
                c=0
        if c==0:
            return 1
        else:
            return 0
s=[]     
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if prime(i)==1 and prime(j)==1 and prime(k)==1:
                if i+j+k==n:
                    if s==[]:
                        s.append(i)
                        s.append(j)
                        s.append(k)
                    elif i<s[0] and j<s[1]:
                        s=[]
                        s.append(i)
                        s.append(j)
                        s.append(k)
                        
print(*s)
