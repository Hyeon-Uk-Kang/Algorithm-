import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
visit=[-1]*(100001)
visit[n]=0

def bfs(start):
    visit[start]=0
    q=deque()
    q.append(start)

    while q:
        x=q.popleft()
        if x==m:
            return visit[m]

        if x-1>=0 and visit[x-1]==-1:
            visit[x-1]=visit[x]+1
            q.append(x-1)
        if x+1<=100000 and visit[x+1]==-1:
            visit[x+1]=visit[x]+1
            q.append(x+1)
        if 2*x<=100000 and visit[2*x]==-1:
            visit[2*x]=visit[x]+1
            q.append(2 * x)

print(bfs(n))
