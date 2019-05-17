n=int(input())
l=[]
for i in range(n):
    s=input()
    
    l.append(s.lower())
k=sorted(l)
for i in range(len(k)):
    print(k[i])
