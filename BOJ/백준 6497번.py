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
while True:
    n,m=map(int,sys.stdin.readline().split())
    if n==0 and m==0:
        break
    parent=[i for i in range(n+1)]
    edge=[]
    total=0
    for i in range(m):
        a,b,c=map(int,sys.stdin.readline().split())
        edge.append((c,a,b))
        total+=c

    edge.sort()
    result=0
    for i in edge:
        dist,a,b=i
        if find(a)!=find(b):
            union(a,b)
            result+=dist
    print(total-result)