from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,l,r=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

def f(x,y):
    global flag
    visit[x][y]=1
    unite=[]
    unite.append((x,y))
    q=deque()
    q.append((x,y))
    cnt=1
    sum=arr[x][y]

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny]==0:
                    if l<=abs(arr[nx][ny]-arr[x][y])<=r:
                        visit[nx][ny]=1
                        flag=1
                        cnt+=1
                        sum+=arr[nx][ny]
                        q.append((nx,ny))
                        unite.append((nx,ny))

    for i,j in unite:
        arr[i][j]=int(sum/cnt)
    #print("flag",flag)

time=0
while True:
    visit=[[0]*n for i in range(n)]
    flag=0
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                f(i,j)

    if flag==0:
        break
    time+=1
print(time)
