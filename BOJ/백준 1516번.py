import sys
import copy
from collections import deque

n=int(input())
time=[0]*(n+1)
arr=[[] for i in range(n+1)]
indegree=[0]*(n+1)

for i in range(1,n+1):
    data=list(map(int,sys.stdin.readline().split()))
    time[i]=data[0]
    for x in data[1:len(data)-1]:
        arr[x].append(i)
        indegree[i]+=1

def topology_sort():

    q=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    result=copy.deepcopy(time)

    while q:
        now=q.popleft()
        for i in arr[now]:
            indegree[i]-=1
            result[i]=max(result[i],time[i]+result[now])
            if indegree[i]==0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])

topology_sort()
