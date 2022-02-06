import sys
import copy
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,m=map(int,sys.stdin.readline().split())

arr=[]
arr2=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr2=copy.deepcopy(arr)

def dfs_on(x,y):
    arr[x][y]=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==0:
                dfs_on(nx,ny)

def dfs_off(x,y):
    arr2[x][y]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr2[nx][ny]==1:
                dfs_off(nx,ny)

cnt1,cnt2=0,0
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            dfs_on(i,j)
            cnt1+=1
        elif arr2[i][j]==1:
            dfs_off(i,j)
            cnt2+=1

print(cnt1,cnt2)