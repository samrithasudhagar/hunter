n=int(input())
s=[]
c=0
if n==1 or n==2:
    print(0)
for i in range(2,n):
    for j in range(2,i):
        if i==2:
            s.append(2)
        else:
            if i%j==0:
                c=c+1
                
                break
            else:
                c=0
    if c==0:
        s.append(i)
print(*s)
    
