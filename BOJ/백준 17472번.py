import sys
from collections import deque
INF=sys.maxsize
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,m=map(int,sys.stdin.readline().split())
arr=[]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

num_map=[[-1]*m for i in range(n)]

num=0

def bfs(x,y,num):
    q=deque()
    q.append((x,y))
    num_map[x][y]=num

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==1 and num_map[nx][ny]==-1:
                    q.append((nx,ny))
                    num_map[nx][ny]=num

for i in range(n):
    for j in range(m):
        if num_map[i][j]==-1 and arr[i][j]==1:
            bfs(i,j,num)
            num+=1

dist=[[INF]*num for i in range(num)]

for i in range(n):
    for j in range(m):
        if arr[i][j]==1 and num_map[i][j]!=-1:
            start=num_map[i][j]
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                b_dist=0

                while 0<=nx<n and 0<=ny<m:
                    if arr[nx][ny]==1:
                        end=num_map[nx][ny]
                        if start==end:
                            break
                        if b_dist==1:
                            break
                        else:
                            dist[start][end]=min(dist[start][end],b_dist)
                            break
                    nx+=dx[k]
                    ny+=dy[k]
                    b_dist+=1

parent=[i for i in range(num)]

edge=[]
for i in range(num):
    for j in range(num):
        if dist[i][j]!=INF:
            edge.append((dist[i][j],i,j))

edge.sort()
result,cnt=0,0

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a!=b:
        parent[b]=a

for i in edge:
    dist,a,b=i
    if find(a)!=find(b):
        union(a,b)
        cnt+=1
        result+=dist

if cnt==num-1:
    print(result)
else:
    print(-1)


