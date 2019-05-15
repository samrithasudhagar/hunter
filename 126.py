s=input()
c=0
l=s.split()
for i in range(len(l)):
   
    if l[i][0].isupper():
        c=c+1
    k=i+1
if c==k:
    print("yes")
else:
    print("no")
