import heapq
INF=10000000000000000000
n,m,k=map(int,input().split())
arr=[[] for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    arr[b].append((a,c))

data=list(map(int,input().split()))
for i in data:
    arr[0].append((i,0))

def dijkstra(start):
    visit[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>visit[now]:
            continue
        for i in arr[now]:
            cost=dist+i[1]
            if cost<visit[i[0]]:
                visit[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

visit=[INF]*(n+1)
dijkstra(0)
ans=0
for i in range(1,n+1):
    if visit[i]!=INF and visit[i]>ans:
        ans=visit[i]
        index=i

print(index)
print(ans)