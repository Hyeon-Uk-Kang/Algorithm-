dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

v=[]
for i in range(m):
    a,b=map(int,input().split())
    v.append((a-1,b))

cloud=[(n-2,0),(n-2,1),(n-1,0),(n-1,1)]

for k in range(m):

    next_cloud=[]
    move=v[k]
    for i in cloud:
        x,y=i[0],i[1]
        di=move[0]
        si=move[1]
        nx=(x+dx[di]*si)%n
        ny=(y+dy[di]*si)%n
        next_cloud.append((nx,ny))

    visit=[[0]*n for i in range(n)]
    for i in next_cloud:
        x,y=i[0],i[1]
        visit[x][y]=1
        arr[x][y]+=1

    cx=[1,1,-1,-1]
    cy=[1,-1,1,-1]
    for i in next_cloud:
        x,y=i[0],i[1]
        cnt=0
        for z in range(4):
            nx=x+cx[z]
            ny=y+cy[z]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]>=1:
                cnt+=1
        arr[x][y]+=cnt

    cloud=[]
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0 and arr[i][j]>=2:
                arr[i][j]-=2
                cloud.append((i,j))

ans=0
for i in range(n):
    for j in range(n):
        ans+=arr[i][j]
print(ans)