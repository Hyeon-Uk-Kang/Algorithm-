from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
n,k,r=map(int,input().split())

arr=[[[0]*(4) for i in range(n+1)]for i in range(n+1)]

for i in range(r):
    x,y,xx,yy=map(int,input().split())
    for z in range(4):
        nx=x+dx[z]
        ny=y+dy[z]
        if nx==xx and ny==yy:
            arr[x][y][z]=1
            arr[xx][yy][(z+2)%4]=1

v=[]
for i in range(k):
    r,c=map(int,input().split())
    v.append((r,c))

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            if arr[x][y][i]==1:
                continue
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=n and 1<=ny<=n:
                if visit[nx][ny]==0:
                    visit[nx][ny]=1
                    q.append((nx,ny))

ans=0
for i in range(k):
    visit=[[0]*(n+1) for i in range(n+1)]
    bfs(v[i][0],v[i][1])

    for j in range(i+1,k):
        if visit[v[j][0]][v[j][1]]==0:
            ans+=1
print(ans)