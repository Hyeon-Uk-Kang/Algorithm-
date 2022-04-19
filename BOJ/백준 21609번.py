from collections import deque
import copy
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(input().split()))

visit=[[0]*n for i in range(n)]

def down():

    for j in range(n):
        while True:
            flag=0
            for i in range(n-1,0,-1):
                if arr[i][j]=='.' and arr[i-1][j]!='.' and arr[i-1][j]!='-1':
                    arr[i][j]=arr[i-1][j]
                    arr[i-1][j]='.'
                    flag=1
            if flag==0:
                break

    '''print("down")
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()
    print()'''

def rotate(x,y):
    global arr
    arr2=[[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            arr2[x+n-j-1][y+i]=arr[x+i][y+j]

    arr=copy.deepcopy(arr2)

    '''print("rotate")
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()
    print()'''
    return arr

def bfs(x,y,k):

    q=deque()
    q.append((x,y))
    visit[x][y]=1

    if arr[x][y]=='0':
        r.append((x,y))
    else:
        v.append((x,y))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny]==0:
                    if arr[nx][ny]==k and arr[nx][ny]!='0':
                        visit[nx][ny]=1
                        q.append((nx,ny))
                        v.append((nx,ny))
                    elif arr[nx][ny]=='0':
                        visit[nx][ny]=1
                        q.append((nx,ny))
                        r.append((nx,ny))

    v.sort()


ans=0

while True:
    check=0
    block_len = -1
    rainbow = -1
    v_x, v_y = -1, -1
    for i in range(n):
        for j in range(n):
            if arr[i][j] != '-1' and arr[i][j] != '.':
                v, r = [], []
                bfs(i, j, arr[i][j])
                visit = [[0] * n for i in range(n)]
                #print(v, r)
                if len(v)>=1 and len(v) + len(r) >= 2:
                    print(i,j,v,r)
                    check=1
                    if len(v) + len(r) > block_len or (len(v) + len(r) == block_len and len(r) > rainbow) or (
                            len(v) + len(r) == block_len and len(r) == rainbow and v[0][0] > v_x) or (
                            len(v) + len(r) == block_len and len(r) == rainbow and v[0][0] == v_x and v[0][1] > v_y):
                        block_len = len(v) + len(r)
                        rainbow = len(r)
                        v_x = v[0][0]
                        v_y = v[0][1]
                        res = []
                        for z in v:
                            res.append(z)
                        for z in r:
                            res.append(z)

    if check==0:
        break

    #print('res',res)

    ans += (len(res) ** 2)
    #print("ans,",ans)
    for x, y in res:
        arr[x][y] = '.'

    '''for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print()'''

    down()
    rotate(0, 0)
    down()


print(ans)





