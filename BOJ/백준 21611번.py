from collections import deque
import copy
dx=[0,1,0,-1]
dy=[-1,0,1,0]
cx=[-1,1,0,0]
cy=[0,0,-1,1]

n,m=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

x,y=n//2,n//2
bomb=[0]*4

def zero():
    global q
    visit = [[0] * n for i in range(n)]
    x,y=n//2,n//2
    visit[x][y] = 1
    dir = 0
    q=deque()

    while True:
        if x == 0 and y == 0:
            break

        nx = x + dx[dir]
        ny = y + dy[dir]

        if visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if arr[nx][ny] != 0:
                q.append(arr[nx][ny])
            x, y = nx, ny
            dir += 1
            if dir == 4:
                dir = 0
        else:
            dir -= 1
            if dir == -1:
                dir = 3

    #print("zero")
    if len(q)==0:
        print(bomb[1]+2*bomb[2]+3*bomb[3])
        #print("sex")
        exit()


def move():
    global arr,q,qq

    #print("큐 길이ㅇㅇㅇㅇㅇㅇㅇㅇㅇ",len(q))
    visit = [[0] * n for i in range(n)]
    x,y=n//2,n//2
    visit[x][y] = 1
    dir = 0
    qq = deque()
    arr=[[0]*n for i in range(n)]

    while q:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if visit[nx][ny] == 0:
            visit[nx][ny] = 1
            bean=q.popleft()
            qq.append(bean)
            arr[nx][ny]=bean
            x, y = nx, ny
            dir += 1
            if dir == 4:
                dir = 0
        else:
            dir -= 1
            if dir == -1:
                dir = 3

    '''print("move")
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()
    print(qq)
    print()'''

def find():
    global qq,q
    idx=0
    cnt=1
    flag=0

    for i in range(1,len(qq)):
        if qq[idx]==qq[i]:
            cnt+=1
        else:
            if cnt>=4:
                bomb[qq[idx]]+=cnt
                for j in range(idx,idx+cnt):
                    qq[j]=0
                    flag=1

            cnt=1
            idx=i

    if cnt==len(qq):
        q = deque()
        if cnt >= 4:
            bomb[qq[idx]] += cnt
            for z in range(cnt):
                q.append(0)
        else:
            for z in range(cnt):
                q.append(qq[idx])

    '''print(bomb)
    print("find")
    print("qq",qq)'''
    q=copy.deepcopy(qq)
    return flag

def make_group():

    global q

    idx=0
    cnt=1
    new_q=deque()
    for i in range(1,len(q)):
        if q[idx]==q[i]:
            cnt+=1
        else:
            new_q.append(cnt)
            new_q.append(q[idx])
            cnt=1
            idx=i
    new_q.append(cnt)
    new_q.append(q[idx])

    q=deque()
    #print("new q",new_q)
    T = (n * n) - 1
    if len(new_q)>T:
        while T > 0:
            x = new_q.popleft()
            q.append(x)
            T -= 1
    else:
        while new_q:
            x=new_q.popleft()
            q.append(x)

    #print("make groupppppppp",q)

for i in range(m):
    di,si=map(int,input().split())
    di-=1

    for k in range(1,si+1):
        nx=x+cx[di]*k
        ny=y+cy[di]*k
        arr[nx][ny]=0

    '''print("처음")
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()'''

    while True:
        zero()
        move()
        chk=find()
        #print("ccccccccchk",chk)
        if chk==0:
            break
        move()

    make_group()
    move()
print(bomb[1]+2*bomb[2]+3*bomb[3])