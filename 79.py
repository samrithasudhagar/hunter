def eveodd(l):
    
    if len(l)%2==1:
        k=len(l)//2
        print(l[k])
    
        l.remove(l[k])
    else:
        p=(len(l)//2)-1
        d=(len(l)//2)
       
        k=(l[p]+l[d])//2
        print(k)
        l.remove(l[p])
        l.remove(l[d-1])
   
    return(l)
n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if len(l)>0:
        l=eveodd(l)
        
