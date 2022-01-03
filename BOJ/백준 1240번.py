import sys
sys.setrecursionlimit(10**9)
n,m=map(int,sys.stdin.readline().split())
arr=[[] for i in range(n+1)]
for i in range(n-1):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

def dfs(x,y,sum):
    visit[x]=1
    if x==y:
        print(sum)
        return sum
    for i in arr[x]:
        if visit[i[0]]==0:
            dfs(i[0],y,sum+i[1])
for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    visit=[0]*(n+1)
    dfs(x,y,0)