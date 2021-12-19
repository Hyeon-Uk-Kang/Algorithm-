import sys
from collections import deque
INF=sys.maxsize

n,m=map(int,sys.stdin.readline().split())
arr=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

s,t=map(int,sys.stdin.readline().split())

start=1
end=INF
ans=0

def bfs(mid):
    global ans, flag
    visit=[0]*(n+1)
    visit[s]=1
    q=deque()
    q.append(s)

    while q:
        now=q.popleft()
        if now==t:
            flag=1
            ans=max(ans,mid)
            break
        for i in arr[now]:
            if visit[i[0]]==0 and i[1]>=mid:
                visit[i[0]]=1
                q.append(i[0])

while start<=end:
    mid=(start+end)//2
    flag=0
    bfs(mid)

    if flag==1:
        start=mid+1
    else:
        end=mid-1
print(ans)