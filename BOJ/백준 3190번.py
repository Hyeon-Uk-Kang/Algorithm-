import sys
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
arr=[[0]*(n+1) for i in range(n+1)]

m=int(input())
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a][b]=2

k=int(input())
v=[]
for i in range(k):
    a,b=input().split()
    v.append((int(a),b))

q=[]
q.append((1,1))
time=0
x,y=1,1
direction=2
index=0
def turn(c,direction):
    if c=='L':
        if direction==0:
            return 2
        elif direction==1:
            return 3
        elif direction==2:
            return 1
        else:
            return 0
    else:
        if direction==0:
            return 3
        elif direction==1:
            return 2
        elif direction==2:
            return 0
        else:
            return 1
while True:
    nx=x+dx[direction]
    ny=y+dy[direction]

    if 1<=nx<=n and 1<=ny<=n and arr[nx][ny]!=1:
        if arr[nx][ny]==2:
            arr[nx][ny]=1
            q.append((nx,ny))
        else:
            px,py=q.pop(0)
            arr[px][py]=0
            arr[nx][ny]=1
            q.append((nx,ny))
    else:
        time+=1
        print(time)
        break

    time+=1

    if index<m and time==v[index][0]:
        direction=turn(v[index][1],direction)
        index+=1

    x,y=nx,ny



