from itertools import permutations
n=list(input())
s=""
p = permutations(n)
b=[]
for i in list(p):
    s=''
    for j in i:
       s+=j
    if s not in b:
       b.append(s)
       print(s)
