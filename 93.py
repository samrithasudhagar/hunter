i=input()
p=""
c=0
for j in range(len(i)):
	if c%2==0:
		p=p+i[j].upper()
		c=c+1
	elif i[j]==" ":
		p=p+" "
	elif c%2==1:
		p=p+i[j]
		c=c+1
		
print(p)
    

#i
