import sys

tc=int(input())

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if b>a:
        parent[b]=a
    elif a>b:
        parent[a]=b
while tc>0:
    n,m,p,q=map(int,sys.stdin.readline().split())
    parent=[i for i in range(n+1)]

    edge=[]
    for i in range(m):
        a,b,c=map(int,sys.stdin.readline().split())
        a=min(a,b)
        b=max(a,b)
        edge.append((c,a,b))

    edge.sort()
    ans=[]
    for i in edge:
        cost,a,b=i
        if find(a)!=find(b):
            union(a,b)
            ans.append(i)
    flag=0
    for i in ans:
        if i[1]==p and i[2]==q:
            flag=1
            break

    if flag==1:
        print("YES")
    else:
        print("NO")
    tc-=1