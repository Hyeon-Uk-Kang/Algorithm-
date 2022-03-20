import sys

tc=int(input())

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])

    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a!=b:
        parent[b]=a

while tc>0:
    n=int(input())
    parent=[i for i in range(n+1)]


    x=[]
    y=[]
    dist=[]
    for i in range(n):
        a,b,r=map(int,sys.stdin.readline().split())
        x.append(a)
        y.append(b)
        dist.append(r)

    ans = n
    for i in range(n-1):
        for j in range(i+1,n):
            if (x[i]-x[j])**2+(y[i]-y[j])**2<=(dist[i]+dist[j])**2:
                if find(i)!=find(j):
                    union(i,j)
                    ans-=1

    print(ans)
    tc-=1