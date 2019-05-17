s=input()
l=list(s)
p=0
for i in range(len(s)):
    p=p+(int(l[i])**len(s))
print(p)
