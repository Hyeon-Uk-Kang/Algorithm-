from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

arr=[]
v=[]
ans=0
for i in range(5):
    arr.append(list(input()))
    for j in range(5):
        v.append((i,j))

s=[0]*len(v)

def bfs():
    global q,visit,arr2
    notgae=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<5 and 0<=ny<5:
                if arr2[nx][ny]==1 and visit[nx][ny]==0:
                    q.append((nx,ny))
                    visit[nx][ny]=1
                    notgae+=1
    return notgae

def dfs(idx,cnt):
    global q,visit,arr2,ans

    if cnt==7:
        s_cnt=0
        k=[]
        for i in range(len(v)):
            if s[i]==1:
                x,y=v[i][0],v[i][1]
                if arr[x][y]=='S':
                    s_cnt+=1
                k.append((x,y))

        if s_cnt>=4:
            arr2=[[0]*5 for i in range(5)]
            visit=[[0]*5 for i in range(5)]
            for i in k:
                x,y=i[0],i[1]
                arr2[x][y]=1

            q=deque()
            q.append((k[0][0],k[0][1]))
            visit[k[0][0]][k[0][1]]=1
            if bfs()==7:
                ans+=1
        return


    for i in range(idx,len(v)):
        s[i]=1
        dfs(i+1,cnt+1)
        s[i]=0

dfs(0,0)
print(ans)