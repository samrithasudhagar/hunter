
i=input()
p=""
for j in range(len(i)):
	if j%2==0:
		p=p+i[j].upper()
	elif i[j]==" ":
		p=p+" "
	else:
		p=p+i[j]
		
print(p)
#i
