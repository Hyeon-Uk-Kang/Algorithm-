import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

m,n=map(int,sys.stdin.readline().split())
arr=[]
visit=[[0]*m for i in range(n)]
q=deque()

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if arr[i][j]==1:
            q.append((i,j))
            visit[i][j]=1
        elif arr[i][j]==-1:
            visit[i][j]=-1

def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0 and visit[nx][ny]==0:
                    q.append((nx,ny))
                    visit[nx][ny]=visit[x][y]+1
bfs()

ans,flag=0,0

for i in range(n):
    for j in range(m):
        if visit[i][j]==0:
            flag=1
        ans=max(ans,visit[i][j])

if flag==1:
    print(-1)
else:
    print(ans-1)