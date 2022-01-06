import sys
input=sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

m,n=map(int,input().split())
arr=[]
cnt_w=[0]*(n*m)
cnt_b=[0]*(n*m)
t1,t2=0,0

for i in range(n):
    arr.append(list(input()))

def dfs_w(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return
    if arr[x][y]=="W":
        arr[x][y]="."
        cnt_w[t1]+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs_w(nx,ny)

def dfs_b(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return
    if arr[x][y]=="B":
        arr[x][y]="."
        cnt_b[t2]+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs_b(nx,ny)

for i in range(n):
    for j in range(m):
        if arr[i][j]=="W":
            dfs_w(i,j)
            t1+=1
        elif arr[i][j]=="B":
            dfs_b(i,j)
            t2+=1

ans1,ans2=0,0

for i in range(t1):
    ans1+=cnt_w[i]*cnt_w[i]

for i in range(t2):
    ans2+=cnt_b[i]*cnt_b[i]

print(ans1,ans2)