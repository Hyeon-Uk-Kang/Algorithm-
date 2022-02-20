import sys

n,m=map(int,sys.stdin.readline().split())
data=list(input().split())
parent=[i for i in range(n+1)]

edge=[]
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

result,total=0,0
for i in edge:
    dist,a,b=i
    if data[a-1]!=data[b-1]:
        if find(a)!=find(b):
            union(a,b)
            result+=dist
            total+=1

if total==n-1:
    print(result)
else:
    print(-1)