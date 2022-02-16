import sys
import math

n,m=map(int,sys.stdin.readline().split())
x,y=[],[]
parent=[i for i in range(n+1)]

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    x.append(a)
    y.append(b)

edge=[]
for i in range(n-1):
    for j in range(i+1,n):
        d=math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
        edge.append((d,i+1,j+1))

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

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    union(a,b)

result=0
for i in edge:
    dist,a,b=i
    if find(a)!=find(b):
        union(a,b)
        result+=dist

print(format(result,".2f"))