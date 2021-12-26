import sys
sys.setrecursionlimit(10**9)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

tc=int(input())

def dfs(x,y):
    arr[x][y]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==1:
                dfs(nx,ny)

while tc>0:
    m,n,k=map(int,sys.stdin.readline().split())
    arr=[[0]*(m) for i in range(n)]

    for i in range(k):
        a,b=map(int,sys.stdin.readline().split())
        arr[b][a]=1

    cnt=0

    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                dfs(i,j)
                cnt+=1

    print(cnt)

    tc-=1