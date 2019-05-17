s=input()
l=0
su=0
for i in range(len(s)+1):
    k=s[:i]
    for i in k:
        su=su+int(i)
print(su)
