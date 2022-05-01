dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

n,m,k=map(int,input().split())

arr=[]
shark=[[] for i in range(m+1)]
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(n):
        if arr[i][j]>0:
            shark[arr[i][j]].append(i)
            shark[arr[i][j]].append(j)
            arr[i][j]=[arr[i][j],k]

data=[0]+list(map(int,input().split()))

for i in range(1,m+1):
    shark[i].append(data[i])

dir=[[] for i in range(m+1)]

for i in range(m):
    for j in range(4):
        dir[i+1].append([0]+list(map(int,input().split())))

ans=0
while True:

    visit=[[0]*n for i in range(n)]

    for i in range(1,m+1):
        if shark[i]!=0:
            x,y,di=shark[i][0],shark[i][1],shark[i][2]
            flag=0
            ndir=dir[i][di-1]
            for z in range(1,5):
                nx=x+dx[ndir[z]]
                ny=y+dy[ndir[z]]
                if 0<=nx<n and 0<=ny<n:
                    if arr[nx][ny]==0:
                        flag=1
                        break

            if flag==0:
                for z in range(1, 5):
                    nx = x + dx[ndir[z]]
                    ny = y + dy[ndir[z]]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny][0] == i:
                            break

            '''if visit[nx][ny]==0:
                visit[nx][ny]=i
                shark[i]=[nx,ny,di]
            else:
                if visit[nx][ny]>i:
                    visit[nx][ny]=i
                    shark[visit[nx][ny]]=0
                else:
                    shark[i]=0'''
            if visit[nx][ny]:
                if visit[nx][ny]<i:
                    shark[i]=0
                else:
                    shark[visit[nx][ny]]=0
            else:
                visit[nx][ny]=i
                shark[i]=[nx,ny,ndir[z]]

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                arr[i][j][1]-=1
                if arr[i][j][1]==0:
                    arr[i][j]=0

    cnt=0
    for i in range(1,m+1):
        if shark[i]:
            x,y=shark[i][0],shark[i][1]
            arr[x][y]=[i,k]
            cnt+=1

    ans+=1
    if cnt==1:
        print(ans)
        break
    if ans == 1001:
        print(-1)
        break