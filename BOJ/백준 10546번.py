n=int(input())
d={}
for i in range(n):
    a=input()
    if a not in d:
        d[a]=1
    else:
        d[a]+=1

for i in range(n-1):
    a=input()
    d[a]-=1

for i,j in d.items():
    if j>0:
        print(i)