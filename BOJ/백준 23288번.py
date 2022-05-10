from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]
n,m,k=map(int,input().split())
dice=[0,1,2,3,4,5,6]

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

dir=0
x,y=0,0
ans=0
def bfs(x,y,k):
    q=deque()
    q.append((x,y))
    visit=[[0]*m for i in range(n)]
    visit[x][y]=1
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny]==0 and arr[nx][ny]==k:
                    q.append((nx,ny))
                    visit[nx][ny]=1
                    cnt+=1

    return cnt

for i in range(k):

    nx=x+dx[dir]
    ny=y+dy[dir]

    ans+=bfs(nx,ny,arr[nx][ny])*arr[nx][ny]

    if dir==0:
        dice[1],dice[3],dice[4],dice[6]=dice[4],dice[1],dice[6],dice[3]
    elif dir==1:
        dice[1],dice[2],dice[5],dice[6]=dice[2],dice[6],dice[1],dice[5]
    elif dir==2:
        dice[1],dice[3],dice[4],dice[6]=dice[3],dice[6],dice[1],dice[4]
    else:
        dice[1],dice[2],dice[5],dice[6]=dice[5],dice[1],dice[6],dice[2]

    if dice[6]>arr[nx][ny]:
        dir+=1
        if dir==4:
            dir=0
    elif dice[6]<arr[nx][ny]:
        dir-=1
        if dir==-1:
            dir=3

    x,y=nx,ny
    if not (0<=x+dx[dir]<n) or not (0<=y+dy[dir]<m):
        dir=(dir+2)%4

print(ans)