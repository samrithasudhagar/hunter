s=input()
k=""
for i in range(len(s)-1,-1,-1):
    if s[i] not in k:
        k=k+s[i]
print(k)
