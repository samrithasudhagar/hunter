s=input()
k=""
if s[-1]==".":
    s=s[:-1]
l=list(s.split(" "))
for i in range(len(l)):
    if i%2==0 and i!=len(l)-1:
        k=k+l[i][::-1]+" "
    elif i%2==1 and i!=len(l)-1:
        k=k+l[i]+" "
    elif i%2==0 and i==len(l)-1:
        k=k+l[i][::-1]
    elif i%2==1 and i==len(l)-1:
        k=k+l[i]
print(k)
    
