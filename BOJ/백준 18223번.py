import sys
import heapq
INF=sys.maxsize

n,m,k=map(int,sys.stdin.readline().split())
arr=[[] for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

def dijkstra(start,end):
    visit=[INF]*(n+1)
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

    return visit[end]

res1=dijkstra(1,n)
res2=dijkstra(1,k)+dijkstra(k,n)

if res1==res2:
    print("SAVE HIM")
else:
    print("GOOD BYE")