import sys
sys.setrecursionlimit(10**9)
n,m,v=map(int,input().split())
arr=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,n+1):
    arr[i].sort()

visit=[0]*(n+1)
cnt=1
def dfs(start):
    global cnt
    visit[start]=cnt

    for i in arr[start]:
        if visit[i]==0:
            cnt+=1
            dfs(i)

dfs(v)

for i in range(1,n+1):
    print(visit[i],end=" ")