import sys
import heapq

n,m=map(int,sys.stdin.readline().split())
arr=[[] for i in range(n+1)]
indegree=[0]*(n+1)
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    indegree[b]+=1

q=[]
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(q,i)

while q:
    now=heapq.heappop(q)
    print(now,end=" ")
    for i in arr[now]:
        indegree[i]-=1
        if indegree[i]==0:
            heapq.heappush(q,i)

