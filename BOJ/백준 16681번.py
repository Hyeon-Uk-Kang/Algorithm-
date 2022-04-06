import heapq
import sys
INF=sys.maxsize
data=list(map(int,input().split()))
height=[0]+list(map(int,input().split()))
n=data[0]
arr=[[] for i in range(n+1)]

for i in range(data[1]):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

def go(start):
    global visit
    visit=[INF]*(n+1)
    visit[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>visit[now]:
            continue
        for i in arr[now]:
            if height[now]<height[i[0]]:
                cost=i[1]+dist
                if cost<visit[i[0]]:
                    visit[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))

def to(start):
    global visit2
    visit2=[INF]*(n+1)
    visit2[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>visit2[now]:
            continue
        for i in arr[now]:
            if height[now]<height[i[0]]:
                cost=i[1]+dist
                if cost<visit2[i[0]]:
                    visit2[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))

ans=0

go(1)
to(n)

for i in range(2,n):
    res=visit[i]+visit2[i]
    #print(res)
    ans=max(ans,height[i]*data[3]-res*data[2])
if ans==0:
    print("Impossible")
else:
    print(ans)