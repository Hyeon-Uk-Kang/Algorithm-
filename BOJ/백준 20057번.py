left =[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01),
              (-1,-1,0.1),(1,-1,0.1),(0,-2,0.05),(0,-1,1)]
right=[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),
              (-1,1,0.1),(1,1,0.1),(0,2,0.05),(0,1,1)]
up = [(-1,-1,0.1),(-1,1,0.1),(0,1,0.07),(0,-1,0.07),(1,-1,0.01),(1,1,0.01),
               (-2,0,0.05),(0,-2,0.02),(0,2,0.02),(-1,0,1)]
down = [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),
                 (1,-1,0.1),(1,1,0.1),(2,0,0.05),(1,0,1)]

dx=[0,1,0,-1]
dy=[-1,0,1,0]

n=int(input())
arr=[]
visit=[[0]*n for i in range(n)]
for i in range(n):
    arr.append(list(map(int,input().split())))

x,y=n//2,n//2
visit[x][y]=1

dir=0
ans=0
def move(x,y,dir):

    global ans
    tmp=0

    if dir==0:
        for i,j,ratio in left:
            if ratio!=1:
                sand=int(arr[x][y]*ratio)
                tmp+=sand
            else:
                sand=arr[x][y]-tmp
            if 0<=x+i<n and 0<=y+j<n:
                arr[x+i][y+j]+=sand
            else:
                ans+=sand

    elif dir==1:
        for i,j,ratio in down:
            if ratio!=1:
                sand=int(arr[x][y]*ratio)
                tmp+=sand
            else:
                sand=arr[x][y]-tmp
            if 0<=x+i<n and 0<=y+j<n:
                arr[x+i][y+j]+=sand
            else:
                ans+=sand

    elif dir==2:
        for i,j,ratio in right:
            if ratio!=1:
                sand=int(arr[x][y]*ratio)
                tmp+=sand
            else:
                sand=arr[x][y]-tmp
            if 0<=x+i<n and 0<=y+j<n:
                arr[x+i][y+j]+=sand
            else:
                ans+=sand

    elif dir==3:
        for i,j,ratio in up:
            if ratio!=1:
                sand=int(arr[x][y]*ratio)
                tmp+=sand
            else:
                sand=arr[x][y]-tmp
            if 0<=x+i<n and 0<=y+j<n:
                arr[x+i][y+j]+=sand
            else:
                ans+=sand

    #print(sand)


while True:
    if x==0 and y==0:
        break

    nx=x+dx[dir]
    ny=y+dy[dir]

    if visit[nx][ny]==0:
        visit[nx][ny]=1
        #print(nx, ny)
        move(nx, ny, dir)
        x, y = nx, ny
        dir+=1
        if dir==4:
            dir=0
    else:
        dir-=1
        if dir==-1:
            dir=3

print(ans)

