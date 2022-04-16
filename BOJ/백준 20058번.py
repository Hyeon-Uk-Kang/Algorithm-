from collections import deque
import copy
dx=[1,-1,0,0]
dy=[0,0,1,-1]
n,q=map(int,input().split())
arr=[]
len_arr=2**n

for i in range(len_arr):
    arr.append(list(map(int,input().split())))

data=list(map(int,input().split()))
def move(x,y,r_size):
    global arr2

    for i in range(r_size):
        for j in range(r_size):
            arr2[x+j][y+r_size-i-1]=arr[x+i][y+j]


def rotate(arr,len_arr,L):
    global arr2

    arr2=[[0]*len_arr for i in range(len_arr)]

    r_size=2**L
    for i in range(0,len_arr,r_size):
        for j in range(0,len_arr,r_size):
            move(i,j,r_size)

    melt=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            ice=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<len(arr) and 0<=ny<len(arr):
                    if arr2[nx][ny]>0:
                        ice+=1

            if ice<3:
                melt.append((i,j))

    for x,y in melt:
        arr2[x][y]-=1

    arr=copy.deepcopy(arr2)
    return arr

for L in data:
    arr=rotate(arr,len_arr,L)

visit=[[0]*len(arr) for i in range(len(arr))]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=1
    cnt=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<len(arr) and 0<=ny<len(arr):
                if arr[nx][ny]>0 and visit[nx][ny]==0:
                    q.append((nx,ny))
                    visit[nx][ny]=1
                    cnt+=1

    v.append(cnt)

v=[]
sum=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]>0:
            sum+=arr[i][j]
        if arr[i][j]>0 and visit[i][j]==0:
            bfs(i,j)
print(sum)
if len(v)==0:
    print(0)
else:
    print(max(v))