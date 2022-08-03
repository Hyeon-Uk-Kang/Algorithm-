dx=[1,-1,0,0]
dy=[0,0,1,-1]
n,m=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

visit=[[0]*m for i in range(n)]
ans=0

def dfs(x,y,sum,cnt):
    global ans

    if cnt==4:
        ans=max(ans,sum)
        return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if visit[nx][ny]==0:
                visit[nx][ny]=1
                dfs(nx,ny,sum+arr[nx][ny],cnt+1)
                visit[nx][ny]=0

def shape1(x,y):
    global ans

    sum=0
    sum=arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x-1][y+1]
    ans=max(ans,sum)


def shape2(x, y):
    global ans

    sum = 0
    sum = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 1]
    ans = max(ans, sum)


def shape3(x, y):
    global ans

    sum = 0
    sum = arr[x][y] + arr[x+1][y + 1] + arr[x+1][y] + arr[x+2][y]
    ans = max(ans, sum)


def shape4(x, y):
    global ans

    sum = 0
    sum = arr[x][y] + arr[x][y + 1] + arr[x-1][y + 1] + arr[x + 1][y + 1]
    ans = max(ans, sum)

for i in range(n):
    for j in range(m):
        visit[i][j]=1
        dfs(i,j,arr[i][j],1)
        visit[i][j]=0
        if i-1>=0 and j+2<m:
            shape1(i,j)
        if i+1<n and j+2<m:
            shape2(i,j)
        if i+2<n and j+1<m:
            shape3(i,j)
        if i+1<n and i-1>=0 and j+1<m:
            shape4(i,j)

print(ans)