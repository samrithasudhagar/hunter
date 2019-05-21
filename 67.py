l=list(map(str,input().split("#")))
m=list(map(str,input().split("#")))
if int(l[1])+int(l[2])+int(l[3])>int(m[1])+int(m[2])+int(m[3]):
    print(l[0])
else:
    print(m[0])
