import sys

n=int(input())
m=int(input())
cnt=0
parent=[i for i in range(n+1)]
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)

    parent[a]=b
for i in range(m):
    x=int(input())
    p=find(x)

    if p==0:
        break
    else:
        union(p,p-1)
        cnt+=1
print(cnt)




