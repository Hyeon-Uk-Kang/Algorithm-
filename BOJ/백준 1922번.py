import sys

n=int(input())
m=int(input())
arr=[]
parent=[i for i in range(n+1)]
edge=[]
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    edge.append((c,a,b))

edge.sort()
result=0

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a
for i in edge:
    dist,a,b=i
    if find(a)!=find(b):
        union(a,b)
        result+=dist

print(result)