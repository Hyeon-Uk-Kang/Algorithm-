from collections import deque
dx=[1,1,1,-1,-1,-1,0,0]
dy=[1,-1,0,1,-1,0,1,-1]

n,m,tc=map(int,input().split())

arr=[[5]*n for i in range(n)]
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))

tree=[[deque() for i in range(n)]for i in range(n)]
for i in range(m):
    x,y,age=map(int,input().split())
    tree[x-1][y-1].append(age)

while tc>0:
    yangboon=[]
    for i in range(n):
        for j in range(n):
            if len(tree[i][j])>0:
                v=[]

                while len(tree[i][j]):
                    age=tree[i][j].pop()
                    v.append(age)
                v.sort()
                sum=0
                for k in v:
                    if arr[i][j]>=k:
                        arr[i][j]-=k
                        tree[i][j].append(k+1)
                    else:
                        sum+=k//2
                yangboon.append((i,j,sum))

    while yangboon:
        x,y,t=yangboon.pop(0)
        arr[x][y]+=t

    for i in range(n):
        for j in range(n):
            if len(tree[i][j])>0:
                for k in tree[i][j]:
                    if k%5==0:
                        for z in range(8):
                            nx=i+dx[z]
                            ny=j+dy[z]
                            if 0<=nx<n and 0<=ny<n:
                                tree[nx][ny].append(1)
            arr[i][j]+=data[i][j]
    tc-=1

cnt=0
for i in range(n):
    for j in range(n):
        cnt+=len(tree[i][j])
print(cnt)