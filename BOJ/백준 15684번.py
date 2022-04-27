INF=100000000000
n,m,h=map(int,input().split())
arr=[[0]*(n+1) for i in range(h+1)]

ans=INF

for i in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1

def check():

    for i in range(1,n+1):
        t=i
        for j in range(1,h+1):
            if arr[j][t]==1:
                t+=1
            elif arr[j][t-1]==1:
                t-=1
        if t!=i:
            return False
    return True

def line(idx,cnt):
    global ans
    print("sex")
    if cnt>=4:
        return

    if check()==True:
        ans=min(ans,cnt)
        print(cnt)
        return

    for i in range(idx,h+1):
        for j in range(1,n):
            if arr[i][j-1]==0 and arr[i][j]==0 and arr[i][j+1]==0:
                arr[i][j]=1
                line(i,cnt+1)
                arr[i][j]=0

line(1,0)
if ans==INF:
    print(-1)
else:
    print(ans)