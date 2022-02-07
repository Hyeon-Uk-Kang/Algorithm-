import sys

n,m=map(int,sys.stdin.readline().split())
parent=[i for i in range(n+1)]
e=[0]*(n+1)

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def unite(a,b):
    a=find(a)
    b=find(b)

    if b>a:
        parent[b]=a
    elif a>b:
        parent[a]=b

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    x=find(a)
    y=find(b)

    if x==y:
        print(0)
        exit()

    if e[x]==0:
        e[x]=y
    else:
        unite(e[x],y)
    if e[y]==0:
        e[y]=x
    else:
        unite(e[y],x)
print(1)