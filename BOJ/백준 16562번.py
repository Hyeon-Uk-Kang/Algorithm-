import sys
INF=int(1e9)
n,m,k=map(int,sys.stdin.readline().split())
money=list(map(int,sys.stdin.readline().split()))
parent=[i for i in range(n+1)]

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

for i in range(1,n+1):
    parent[i]=find(i)

t=max(parent)
v=[]

for i in range(1,t+1):
    sum=INF
    for j in range(1,n+1):
        if parent[j]==i:
            if sum>money[j-1]:
                sum=money[j-1]
    v.append(sum)

ans=0
for i in v:
    if i!=INF:
        ans+=i

if ans>k:
    print("Oh no")
else:
    print(ans)
