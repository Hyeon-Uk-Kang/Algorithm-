import sys
sys.setrecursionlimit(10**9)

n=int(input())
m=int(input())

arr=[[0]*(n+1) for i in range(n+1)]
visit=[0]*(n+1)

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a][b]=1
    arr[b][a]=1

cnt=0

def dfs(start):
    global cnt
    visit[start]=1

    for i in range(1,n+1):
        if arr[start][i]==1 and visit[i]==0:
            dfs(i)
            cnt+=1
dfs(1)

print(cnt)