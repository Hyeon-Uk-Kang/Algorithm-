import sys
from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]
hdx=[2,2,-2,-2,1,1,-1,-1]
hdy=[1,-1,1,-1,2,-2,2,-2]

k=int(input())
m,n=map(int,sys.stdin.readline().split())
arr=[]
visit=[[[-1]*m for i in range(n)]for i in range(k+1)]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

def bfs():
    q=deque()
    q.append((0,0,0))
    visit[0][0][0]=0

    while q:
        z,x,y=q.popleft()

        if x==n-1 and y==m-1:
            return visit[z][x][y]
        if z<k:
            for i in range(8):
                nx=x+hdx[i]
                ny=y+hdy[i]
                if 0<=nx<n and 0<=ny<m:
                    if arr[nx][ny]==0 and visit[z+1][nx][ny]==-1:
                        q.append((z+1,nx,ny))
                        visit[z+1][nx][ny]=visit[z][x][y]+1

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0 and visit[z][nx][ny]==-1:
                    q.append((z,nx,ny))
                    visit[z][nx][ny]=visit[z][x][y]+1

    return -1
print(bfs())