s=input()
k=s.split()
for i in range(len(k)):
	if i!=0 and i!=len(k):
		print(" ",end="")
	for j in range(len(k[i])-1,-1,-1):
		print(k[i][j],end="")
		
