import sys
INF=int(1e9)
n,v=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j]>arr[i][k]+arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

ans=INF
visit=[0]*n
def dfs(start,sum,cnt):
    global ans
    visit[start]=1
    if sum>ans:
        return
    if cnt==n:
        ans=min(ans,sum)
        return
    for i in range(n):
        if visit[i]==0:
            dfs(i,arr[start][i]+sum,cnt+1)
            visit[i]=0

dfs(v,0,1)
print(ans)