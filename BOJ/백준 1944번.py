import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]
n,m=map(int,sys.stdin.readline().split())
cnt=0
arr=[]
v=[]

for i in range(n):
    arr.append(list(input()))
    for j in range(n):
        if arr[i][j]=='S' or arr[i][j]=='K':
            v.append((i,j))

key=[[0]*(m+1) for i in range(m+1)]

def bfs(x,y,ex,ey):
    q=deque()
    q.append((x,y))
    visit[x][y]=1

    while q:
        x,y=q.popleft()
        if x==ex and y==ey:
            return visit[x][y]-1

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]!='1' and visit[nx][ny]==0:
                    q.append((nx,ny))
                    visit[nx][ny]=visit[x][y]+1

    return -1

for i in range(len(v)-1):
    for j in range(i+1,len(v)):
        visit=[[0]*n for i in range(n)]
        key[i][j]=bfs(v[i][0],v[i][1],v[j][0],v[j][1])
        if key[i][j]==-1:
            print(-1)
            exit()

t=len(v)

parent=[i for i in range(t)]

edge=[]

for i in range(t):
    for j in range(t):
        if key[i][j]!=0:
            edge.append((key[i][j],i,j))

edge.sort()
result,cnt=0,0

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def unite(a,b):
    a=find(a)
    b=find(b)
    if b>a:
        parent[b]=a
    else:
        parent[a]=b
for i in edge:
    cost,a,b=i

    if find(a)!=find(b):
        unite(a,b)
        result+=cost
        cnt+=1

print(result)
