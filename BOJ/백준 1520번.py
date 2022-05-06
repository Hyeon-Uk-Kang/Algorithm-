dx=[1,-1,0,0]
dy=[0,0,1,-1]
n,m=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

dp=[[-1]*m for i in range(n)]
def dfs(x,y):

    if x==n-1 and y==m-1:
        return 1

    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]<arr[x][y]:
                dp[x][y]+=dfs(nx,ny)

    return dp[x][y]
print(dfs(0,0))