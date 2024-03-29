import sys
from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,m=map(int,sys.stdin.readline().split())
arr=[]
visit=[[[0]*m for i in range(n)]for i in range(2)]

for i in range(n):
    arr.append(list(map(int,input())))

def bfs():
    q=deque()
    q.append((0,0,0))
    visit[0][0][0]=1

    while q:
        z,x,y=q.popleft()

        if x==n-1 and y==m-1:
            return visit[z][x][y]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if z==0 and arr[nx][ny]==1 and visit[z+1][nx][ny]==0:
                    q.append((z+1,nx,ny))
                    visit[z+1][nx][ny]=visit[z][x][y]+1
                elif arr[nx][ny]==0 and visit[z][nx][ny]==0:
                    q.append((z,nx,ny))
                    visit[z][nx][ny]=visit[z][x][y]+1
    return -1

print(bfs())