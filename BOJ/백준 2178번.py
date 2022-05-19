import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,m=map(int,sys.stdin.readline().split())

arr=[]
visit=[[0]*m for i in range(n)]

for i in range(n):
    arr.append(list(map(int,input())))

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=1

    while q:
        x,y=q.popleft()

        if x==n-1 and y==m-1:
            return visit[x][y]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==1 and visit[nx][ny]==0:
                    q.append((nx,ny))
                    visit[nx][ny]=visit[x][y]+1
print(bfs(0,0))

