n=int(input())

d={}

for i in range(n):
    a,b=input().split('.')
    if b not in d:
        d[b]=1
    else:
        d[b]+=1

d=sorted(d.items(),key=lambda x:x[0])
for i,j in d:
    print(i,end=" ")
    print(j)