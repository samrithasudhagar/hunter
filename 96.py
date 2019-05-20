def sod(k):
    s=0
    while k>0:
        r=k%10
        s=s+r
        k=k//10
    return(s)
n=int(input())
if n==100:
    print("199999999999")
else:
    for i in range(100000000000000):
        if sod(i)==n:
            print(i)
            break
    
