import sys
import heapq
INF=sys.maxsize

n,m=map(int,sys.stdin.readline().split())
arr=[[] for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

route=[0]*(n+1)
def dijkstra():

    visit=[INF]*(n+1)
    visit[1]=0
    q=[]
    heapq.heappush(q,(0,1))

    while q:
        dist,now=heapq.heappop(q)
        if dist>visit[now]:
            continue

        for i in arr[now]:
            cost=dist+i[1]
            if cost<visit[i[0]]:
                visit[i[0]]=cost
                route[i[0]]=now
                heapq.heappush(q,(cost,i[0]))
dijkstra()

def dijk2(sx,ex):

    visit=[INF]*(n+1)
    visit[1]=0
    q=[]
    heapq.heappush(q,(0,1))

    while q:
        dist,now=heapq.heappop(q)
        if dist>visit[now]:
            continue
        for i in arr[now]:
            if (now==sx and i[0]==ex) or (now==ex and i[0]==sx):
                continue
            cost=dist+i[1]
            if cost<visit[i[0]]:
                visit[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return visit[n]

here=n
ans=0
while here!=0:
    ans=max(ans,dijk2(route[here],here))
    here=route[here]

print(ans)