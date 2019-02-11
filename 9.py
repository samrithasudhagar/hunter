n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
        for j in range(i+1,n):
                if l[i]+l[j]==0:
                        print(l[i],l[j])
                        break
                elif l[i]<0 or l[j]<0:
                        if l[i]+l[j]==-1 or l[i]+l[j]==1:
                                print(l[i],l[j])
                                break
