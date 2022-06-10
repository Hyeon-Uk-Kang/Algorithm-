from collections import deque
import sys
n=int(input())
arr=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

q=deque()
q.append(1)
visit=[0]*(n+1)
visit[1]=1
depth=[0]*(n+1)
p=[0]*(n+1)

while q:
    now=q.popleft()
    for i in arr[now]:
        if visit[i]==0:
            visit[i]=1
            depth[i]=depth[now]+1
            q.append(i)
            p[i]=now

t=int(input())

def lca(a,b):

    if depth[a]>depth[b]:
        a,b=b,a

    while depth[a]!=depth[b]:
        b=p[b]

    while a!=b:
        a=p[a]
        b=p[b]

    return a


for i in range(t):
    a,b=map(int,sys.stdin.readline().split())
    print(lca(a,b))