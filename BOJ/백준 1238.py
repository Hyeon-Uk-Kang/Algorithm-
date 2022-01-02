import sys
import heapq

n,m,x=map(int,sys.stdin.readline().split())

arr=[[] for i in range(n+1)]
time=[0]*(n+1)

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append((b,c))

def dijkstra(start,end):
    q=[]
    INF = int(1e9)
    visit = [INF] * (n + 1)
    heapq.heappush(q,(0,start))
    visit[start]=0

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


for i in range(1,n+1):
    if i==x:
        continue
    time[i]=dijkstra(i,x)+dijkstra(x,i)

print(max(time))