import sys

n,m=map(int,sys.stdin.readline().split())
edge=[]
parent=[i for i in range(n+1)]
arr=[]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    edge.append((c,a,b))

edge.sort()

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a!=b:
        parent[b]=a

result=0
for i in edge:
    c,a,b=i
    if find(a)!=find(b):
        union(a,b)
        result+=c

print(result)