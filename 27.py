s=input()
for i in range(len(s)-1,-1,-1):
    if s[:i+1]!=s[:i+1][::-1]:
        print(s[:i+1])
        break
