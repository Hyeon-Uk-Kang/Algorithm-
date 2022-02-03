import sys
from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

n,m=map(int,sys.stdin.readline().split())
arr=[[0]*(n+1) for i in range(n+1)]
parent=[i for i in range(m+1)]
q=deque()

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a][b]=i+1
    q.append((a,b))

qq=deque()
time=0

while True:
    while q:
        x,y=q.popleft()
        qq.append((x,y))
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=n and 1<=ny<=n:
                if arr[nx][ny]!=0:
                    if find(arr[nx][ny])!=find(arr[x][y]):
                        union(arr[nx][ny],arr[x][y])
                        m-=1

    if m==1:
        print(time)
        break
    time += 1

    while qq:
        x,y=qq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=n and 1<=ny<=n:
                if arr[nx][ny]==0:
                    arr[nx][ny]=arr[x][y]
                    q.append((nx,ny))
                elif arr[nx][ny]!=0:
                    if find(arr[nx][ny])!=find(arr[x][y]):
                        union(arr[nx][ny],arr[x][y])
                        m-=1

