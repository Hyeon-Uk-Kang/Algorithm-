import heapq
INF=100000000000000000
n,m,k=map(int,input().split())

arr=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

left=1
right=1000001

def dijkstra(start,limit):

    visit=[INF]*(n+1)
    visit[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>visit[now]:
            continue
        for i in arr[now]:
            if i[1]>limit:
                if dist+1<visit[i[0]]:
                    visit[i[0]]=dist+1
                    heapq.heappush(q,(dist+1,i[0]))
            else:
                if dist<visit[i[0]]:
                    visit[i[0]] = dist
                    heapq.heappush(q, (dist, i[0]))

    #print(visit)
    if visit[n]>k:
        return False
    else:
        return True

ans=INF
while left<=right:
    mid=(left+right)//2
    flag=dijkstra(1,mid)
    if flag==True:
        ans=mid
        right=mid-1
    else:
        left=mid+1

if ans==INF:
    print(-1)
else:
    print(ans)