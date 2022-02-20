import sys

n=int(input())
parent=[i for i in range(n+1)]

arr=[]
edge=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        edge.append((arr[i][j],i,j))

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