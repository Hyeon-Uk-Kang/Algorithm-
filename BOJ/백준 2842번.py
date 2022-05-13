import sys
from collections import deque
dx=[1,1,1,-1,-1,-1,0,0]
dy=[1,-1,0,1,-1,0,1,-1]
n=int(input())
arr=[]
home=0
for i in range(n):
    arr.append(list(input()))
    for j in range(n):
        if arr[i][j]=="K":
            home+=1
        elif arr[i][j]=="P":
            sx,sy=i,j

fatigue=[]
tire=[]
for i in range(n):
    tire.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        fatigue.append((tire[i][j]))

fatigue=sorted(set(fatigue))
left,right=0,0
INF=int(1e9)
ans=INF
while left<len(fatigue):
    visit=[[0]*n for i in range(n)]
    q=deque()
    tired=tire[sx][sy]
    k=0

    if fatigue[left]<=tired<=fatigue[right]:
        q.append((sx,sy))
        visit[sx][sy]=1

    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
                tired=tire[nx][ny]
                if fatigue[left]<=tired<=fatigue[right]:
                    q.append((nx,ny))
                    visit[nx][ny]=1
                    if arr[nx][ny]=="K":
                        k+=1
    if k==home:
        ans=min(ans,fatigue[right]-fatigue[left])
        left+=1
    elif right+1<len(fatigue):
        right+=1
    else:
        break
print(ans)

