s=input()
m=""
for i in range(len(s)-1):
    for j in range(i+1,len(s)+1):
        kk=s[i:j+1]
        if len(kk)>len(m) and kk==kk[::-1]:
            m=s[i:j]
print(m)
