from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

visit=[[0]*n for i in range(n)]
num=1

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=num

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny]==0 and arr[nx][ny]==1:
                    q.append((nx,ny))
                    visit[nx][ny]=num

for i in range(n):
    for j in range(n):
        if visit[i][j]==0 and arr[i][j]==1:
            bfs(i,j)
            num+=1


def bfs2():

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny]==-1 and arr[nx][ny]==0:
                    q.append((nx,ny))
                    dist[nx][ny]=dist[x][y]+1
                if arr[nx][ny]==1 and visit[nx][ny]!=k:
                    return dist[x][y]

ans=201
for k in range(1,num):
    q=deque()
    dist=[[-1]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j]==k:
                q.append((i,j))
                dist[i][j]=0
    ans=min(ans,bfs2())
print(ans)