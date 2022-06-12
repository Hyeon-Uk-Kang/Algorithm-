from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,m=map(int,input().split())
v=[0,deque(),deque()]
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(m):
        if arr[i][j]>=1:
            v[arr[i][j]].append((i,j))

cnt1,cnt2,cnt3=1,1,0
while v[1] or v[2]:

    tmp1,tmp2=set(),set()

    while v[1]:
        x,y=v[1].popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0:
                    tmp1.add((nx,ny))

    while v[2]:
        x,y=v[2].popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0:
                    tmp2.add((nx, ny))

    tmp3=tmp1 & tmp2

    for x,y in tmp3:
        arr[x][y]=3
        cnt3+=1

    for x,y in tmp1-tmp2:
        arr[x][y]=1
        v[1].append((x,y))
        cnt1+=1

    for x,y in tmp2-tmp1:
        arr[x][y]=2
        v[2].append((x,y))
        cnt2+=1

print(cnt1,cnt2,cnt3)
