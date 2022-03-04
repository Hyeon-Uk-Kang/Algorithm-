import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

parent=[i for i in range(n)]

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

edge=[]
arr=[[] for i in range(1001)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    edge.append((c,a,b))

result=0
edge.sort()
for i in edge:
    cost,a,b=i
    if find(a)!=find(b):
        unite(a,b)
        result+=cost
        arr[a].append((b, cost))
        arr[b].append((a, cost))

print(result)
ans=0
def dfs(x,sum):
    global ans

    visit[x]=1
    if ans<sum:
        ans=sum
    for i in arr[x]:
        if visit[i[0]]==0:
            dfs(i[0],sum+i[1])

for i in range(n):
    visit = [0] * n
    dfs(i, 0)

print(ans)