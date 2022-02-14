import sys
import math
n=int(input())
arr=[]
parent=[i for i in range(n+1)]
for i in range(n):
    a,b=map(float,sys.stdin.readline().split())
    arr.append((a,b))

edge=[]
for i in range(n-1):
    for j in range(i+1,n):
        d=math.sqrt((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)
        edge.append((d,i,j))

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
    dist,a,b=i
    if find(a)!=find(b):
        union(a,b)
        result+=dist
print(format(result,".2f"))