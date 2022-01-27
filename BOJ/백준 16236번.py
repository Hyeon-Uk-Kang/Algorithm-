import sys
from collections import deque
INF=sys.maxsize
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if arr[i][j]==9:
            arr[i][j]=0
            sx,sy=i,j

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny]==-1 and arr[nx][ny]<=now_size:
                    q.append((nx,ny))
                    visit[nx][ny]=visit[x][y]+1

result=0
ate=0
now_size=2
while True:
    visit=[[-1]*n for i in range(n)]
    bfs(sx,sy)

    dist=INF
    for i in range(n):
        for j in range(n):
            if visit[i][j]!=-1 and 1<=arr[i][j]<now_size:
                if dist>visit[i][j]:
                    dist=visit[i][j]
                    x,y=i,j

    if dist==INF:
        print(result)
        break

    result+=dist
    ate+=1
    sx,sy=x,y
    arr[x][y]=0
    if now_size==ate:
        ate=0
        now_size+=1

