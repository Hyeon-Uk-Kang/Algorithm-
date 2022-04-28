import copy
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

arr=[[0]*4 for i in range(4)]
for i in range(4):
    data=list(map(int,input().split()))
    for j in range(4):
        arr[i][j]=[data[j*2],data[j*2+1]-1]

ans=0

def move(arr,x,y,dir):

    while True:
        nx=x+dx[dir]
        ny=y+dy[dir]
        arr[x][y][1]=dir

        if 0<=nx<4 and 0<=ny<4 and arr[nx][ny][0]>=0:
            tmpnum=arr[x][y][0]
            tmpdir=arr[x][y][1]
            arr[x][y][0]=arr[nx][ny][0]
            arr[x][y][1]=arr[nx][ny][1]
            arr[nx][ny][0]=tmpnum
            arr[nx][ny][1]=tmpdir
            break
        else:
            dir+=1
            if dir==8:
                dir=0

def find(arr):

    for num in range(1,17):
        flag=0
        for i in range(4):
            for j in range(4):
                if arr[i][j][0]==num:
                    move(arr,i,j,arr[i][j][1])
                    flag=1
                    break
            if flag==1:
                break

def dfs(arr,sx,sy,sum):
    global ans

    ans=max(ans,sum)

    dir=arr[sx][sy][1]
    arr[sx][sy][0]=-1
    arr[sx][sy][1]=-1
    find(arr)

    tmp=copy.deepcopy(arr)
    for i in range(1,4):
        nx=sx+dx[dir]*i
        ny=sy+dy[dir]*i

        if 0<=nx<4 and 0<=ny<4:
            if arr[nx][ny][0]>0:
                tmp[sx][sy][0]=0
                tmp[sx][sy][1]=0
                dfs(tmp,nx,ny,sum+tmp[nx][ny][0])
                tmp=copy.deepcopy(arr)
        else:
            break

dfs(arr,0,0,arr[0][0][0])
print(ans)