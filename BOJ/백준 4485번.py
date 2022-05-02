import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]
INF=int(1e9)

t=0

while True:
    n=int(input())

    if n==0:
        break

    arr=[]
    q=deque()
    visit=[[INF]*n for i in range(n)]

    for i in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))

    def bfs():
        q.append((0,0))
        visit[0][0]=arr[0][0]
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visit[nx][ny]>visit[x][y]+arr[nx][ny]:
                        visit[nx][ny]=visit[x][y]+arr[nx][ny]
                        q.append((nx,ny))

        print("Problem",end=" ")
        print(t,end="")
        print(":",end=" ")
        print(visit[n-1][n-1])
    t+=1
    bfs()