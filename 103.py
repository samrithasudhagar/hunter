n=int(input())
k=0
for i in range(n):
    for j in range(0,i+k+1):
        print(1,end="")
    k=k+1
    print(end="\n")
