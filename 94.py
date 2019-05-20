s=input()
j=0
k=""
for i in range(len(s)):
    if s[i]==" ":
        mm=s[j:i][::-1]
        k=k+mm
        k=k+" "
        j=i+1
    elif i==len(s)-1:
        mm=s[j:len(s)][::-1]
        k=k+mm
print(k)
