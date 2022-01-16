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

n,m=map(int,sys.stdin.readline().split())
parent=[i for i in range(n+1)]
edge=[]
total=0
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    edge.append((c,a,b))
    total+=c

edge.sort()
result,sum=0,0
for i in edge:
    cost,a,b=i
    if find(a)!=find(b):
        union(a,b)
        result+=cost
        sum+=1

if sum==n-1:
    print(total-result)
else:
    print(-1)