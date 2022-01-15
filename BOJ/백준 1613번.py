import sys
INF=int(1e9)

n,m=map(int,sys.stdin.readline().split())
arr=[[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            arr[i][j]=0

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]>arr[i][k]+arr[k][j]:
                arr[i][j]=1

t=int(input())

for i in range(t):
    x,y=map(int,sys.stdin.readline().split())

    if arr[x][y]==INF and arr[y][x]==INF:
        print(0)
    elif arr[x][y]==1 and arr[y][x]==INF:
        print(-1)
    elif arr[x][y]==INF and arr[y][x]==1:
        print(1)