import sys
sys.setrecursionlimit(10**9)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input())))

cnt=0
result=[]

def dfs(x,y):
    global t

    arr[x][y]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny]==1:
                dfs(nx,ny)
                t+=1

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            t=1
            dfs(i,j)
            result.append(t)
            cnt+=1

result.sort()

print(cnt)

for i in result:
    print(i)
