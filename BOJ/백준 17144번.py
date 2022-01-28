import copy
import sys
dx=[1,-1,0,0]
dy=[0,0,1,-1]
n,m,t=map(int,sys.stdin.readline().split())
arr=[]
v=[]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if arr[i][j]==-1:
            v.append((i,j))

ux,uy=v[0][0],v[0][1]
dx_,dy_=v[1][0],v[1][1]

def move():
    temp=[[0]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j]>0:
                cnt=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<n and 0<=ny<m and arr[nx][ny]!=-1:
                        cnt+=1
                        temp[nx][ny]+=arr[i][j]//5
                temp[i][j]+=arr[i][j]-arr[i][j]//5*cnt
    return temp

def clear(x,y,dir):

    temp=copy.deepcopy(arr)
    arr[x][y]=-1

    cx,cy=x,y
    for i in dir:
        while True:
            nx=x+dx[i]
            ny=y+dy[i]
            if nx==cx and ny==cy:
                return
            if 0<=nx<n and 0<=ny<m:
                arr[nx][ny]=temp[x][y]
            else:
                break
            x,y=nx,ny



while t>0:
    arr=move()
    clear(ux,uy,[2,1,3,0])
    clear(dx_,dy_,[2,0,3,1])
    t-=1
ans=0
for i in range(n):
    for j in range(m):
        if arr[i][j]>0:
            ans+=arr[i][j]
print(ans)