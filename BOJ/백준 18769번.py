import sys

tc=int(input())

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
while tc>0:
    n,m=map(int,sys.stdin.readline().split())
    parent=[i for i in range(n*m+1)]

    edge=[]
    cnt=1
    for i in range(n):
        data=list(map(int,sys.stdin.readline().split()))
        for j in data:
            edge.append((j,cnt,cnt+1))
            cnt+=1
        cnt+=1

    cnt=1
    for i in range(n-1):
        data=list(map(int,sys.stdin.readline().split()))
        for j in data:
            edge.append((j,cnt,cnt+m))
            cnt+=1

    edge.sort()
    result=0
    for i in edge:
        cost,a,b=i
        if find(a)!=find(b):
            unite(a,b)
            result+=cost

    print(result)
    tc-=1