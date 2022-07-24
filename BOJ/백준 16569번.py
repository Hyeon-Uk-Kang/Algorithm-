from collections import deque
INF=1000000000000000
dx=[1,-1,0,0]
dy=[0,0,1,-1]
n,m,k=map(int,input().split())
sx,sy=map(int,input().split())
sx-=1
sy-=1

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

volcano_time=[[INF]*m for i in range(n)]
volcano_map=[[0]*m for i in range(n)]

v=[]
for i in range(k):
    x,y,t=map(int,input().split())
    x-=1
    y-=1
    v.append((x,y,t))
    volcano_map[x][y]=-1

for i in range(len(v)):
    x=v[i][0]
    y=v[i][1]
    time=v[i][2]
    q=deque()
    q.append((x,y))
    #volcano_time[x][y]=time
    t=time+1

    while q:
        for z in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if volcano_time[nx][ny]>t:
                        volcano_time[nx][ny]=t
                        q.append((nx,ny))
        t+=1

q=deque()
q.append((sx,sy,0))
high,short=0,0
visit=[[0]*m for i in range(n)]

while q:
    x,y,t=q.popleft()

    if arr[x][y]>high:
        high=arr[x][y]
        short=t

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        nt=t+1
        if 0<=nx<n and 0<=ny<m:
            if visit[nx][ny]==0:
                visit[nx][ny]=1
                if volcano_map[nx][ny]==-1:
                    continue
                if volcano_time[nx][ny]>nt:
                    q.append((nx,ny,nt))


print(high,short)

