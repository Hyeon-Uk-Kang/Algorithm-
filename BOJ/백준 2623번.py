import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
arr=[[] for i in range(n+1)]
indegree=[0]*(n+1)
result=[]

for k in range(m):
    data=list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(data)-1):
        for j in range(i+1,len(data)):
            arr[data[i]].append(data[j])
            indegree[data[j]]+=1

def topology_sort():

    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        result.append(now)
        for i in arr[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

topology_sort()

if len(result)==n:
    for i in result:
        print(i)
else:
    print(0)