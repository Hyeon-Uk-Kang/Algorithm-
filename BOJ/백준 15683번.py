from collections import deque
import copy

dx=[1,-1,0,0]
dy=[0,0,1,-1]
d=[[[0],[1],[2],[3]],[[2,3],[0,1]],[[1,2],[2,0],[0,3],[1,3]],[[3,1,2],[1,2,0],[2,0,3],[0,3,1]],[[0,1,2,3]]]
n,m=map(int,input().split())

arr=[]
q=deque()
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(m):
        if arr[i][j]>0 and arr[i][j]!=6:
            q.append((i,j,arr[i][j]))

ans=1000000000000000
def check(x,y,dir,visit):

    for i in dir:
        nx=x+dx[i]
        ny=y+dy[i]
        while 0<=nx<n and 0<=ny<m:
            if visit[nx][ny]!=6:
                visit[nx][ny]='#'
            else:
                break
            nx+=dx[i]
            ny+=dy[i]


def dfs(arr,cnt):
    global ans
    visit=copy.deepcopy(arr)

    if cnt==len(q):
        t=0
        for i in range(n):
            for j in range(m):
                if visit[i][j]==0:
                    t+=1
        ans=min(ans,t)
        return

    x,y,num=q[cnt]
    for i in d[num-1]:
        check(x,y,i,visit)
        dfs(visit,cnt+1)
        visit=copy.deepcopy(arr)

dfs(arr,0)
print(ans)