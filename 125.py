s=input()
k=""
for i in range(len(s)):
        if s.count(s[i])==1:
            k=k+str(s[i])
print(k)
