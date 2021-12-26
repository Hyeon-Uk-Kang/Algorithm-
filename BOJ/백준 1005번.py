import sys
from collections import deque
import copy
tc=int(input())
while tc>0:
    n,k=map(int,sys.stdin.readline().split())
    time=list(map(int,sys.stdin.readline().split()))
    indegree=[0]*(n+1)
    arr=[[] for i in range(n+1)]

    for i in range(k):
        a,b=map(int,sys.stdin.readline().split())
        arr[a].append(b)
        indegree[b]+=1

    q=deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    result = copy.deepcopy(time)
    while q:
        now=q.popleft()

        for i in arr[now]:
            indegree[i]-=1
            result[i-1]=max(result[i-1],time[i-1]+result[now-1])
            if indegree[i]==0:
                q.append(i)
    w=int(input())
    print(result[w-1])

    tc-=1


