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
arr=[]
q=deque()
v=[]
parent=[i for i in range(n*m+1)]
lake=[[0]*m for i in range(n)]
cnt=1
for i in range(n):
    arr.append(list(input()))
    for j in range(m):
        if arr[i][j]=='L':
            v.append((i,j))
        if arr[i][j]=='L' or arr[i][j]=='.':
            q.append((i,j))
            lake[i][j]=cnt
            cnt+=1

time=0
qq=deque()
while True:
    while q:
        x,y=q.popleft()
        qq.append((x,y))
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if lake[nx][ny]!=0:
                    if lake[nx][ny]!=lake[x][y]:
                        union(lake[nx][ny],lake[x][y])

    if find(lake[v[0][0]][v[0][1]])==find(lake[v[1][0]][v[1][1]]):
        print(time)
        break

    time += 1

    while qq:
        x,y=qq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if lake[nx][ny]==0:
                    q.append((nx,ny))
                    lake[nx][ny]=lake[x][y]



