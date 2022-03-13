import sys
import copy
from collections import deque

n,m=map(int,sys.stdin.readline().split())
arr=[[] for i in range(n+1)]
indegree=[0]*(n+1)
time=[1]*(n+1)

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    indegree[b]+=1

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

result=copy.deepcopy(time)
while q:
    now=q.popleft()
    for i in arr[now]:
        indegree[i]-=1
        result[i]=max(result[i],result[now]+time[i])
        if indegree[i]==0:
            q.append(i)

for i in range(1,n+1):
    print(result[i],end=" ")