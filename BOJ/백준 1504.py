import sys
import heapq

n,m=map(int,sys.stdin.readline().split())
INF=int(1e9)
arr=[[] for i in range(n+1)]


for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

x,y=map(int,sys.stdin.readline().split())

def dijkstra(start,end):
    q=[]
    visit = [INF] * (n + 1)
    heapq.heappush(q,(0,start))
    visit[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if dist>visit[now]:
            continue
        for i in arr[now]:
            cost=i[1]+dist
            if cost<visit[i[0]]:
                visit[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return visit[end]

res1=dijkstra(1,x)+dijkstra(x,y)+dijkstra(y,n)
res2=dijkstra(1,y)+dijkstra(y,x)+dijkstra(x,n)

if res1>=INF and res2>=INF:
    print(-1)
else:
    print(min(res1,res2))