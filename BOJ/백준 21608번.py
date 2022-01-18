import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
arr=[[0]*n for i in range(n)]
like=[[] for i in range(n*n+1)]

for _ in range(n*n):
    data=list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(data)):
        like[data[0]].append(data[i])

    maxlike=-1
    maxempty=-1
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                likecnt,emptycnt=0,0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny]==0:
                            emptycnt+=1
                        if arr[nx][ny] in like[data[0]]:
                            likecnt+=1
                if maxlike<likecnt or (likecnt==maxlike and maxempty<emptycnt):
                    maxlike=likecnt
                    maxempty=emptycnt
                    x=i
                    y=j

    arr[x][y]=data[0]

ans=0
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] in like[arr[i][j]]:
                    cnt+=1
        if cnt==0:
            ans+=0
        elif cnt==1:
            ans+=1
        elif cnt==2:
            ans+=10
        elif cnt==3:
            ans+=100
        else:
            ans+=1000
print(ans)