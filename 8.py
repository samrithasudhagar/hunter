n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if i<j<k:
                if l[i]+l[j]==l[k]:
                    print(l[i],end=" ")
                    print(l[j],end=" ")
                    print(l[k])
        
    
