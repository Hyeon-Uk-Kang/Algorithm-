import sys

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])

    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a!=b:
        parent[b]=a

n,m,k=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
parent=[i for i in range(n+1)]
edge=[]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    edge.append((c,a,b))

for i in range(k-1):
    union(data[i],data[i+1])

edge.sort()
result=0
for i in edge:
    cost,a,b=i
    if find(a)!=find(b):
        union(a,b)
        result+=cost

print(result)