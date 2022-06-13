from collections import deque

n=int(input())
arr=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

data=list(map(int,input().split()))
visit=[-1]*(n+1)
visit[1]=0
depth=[[] for i in range(n+1)]

q=deque()
q.append(1)
while q:
    now=q.popleft()
    for i in arr[now]:
        if visit[i]==-1:
            q.append(i)
            visit[i]=visit[now]+1
            depth[now].append(i)

idx=1
flag=0
#print(depth)
for i in data:
    if idx==n:
        break

    c=len(depth[i])
    c1=data[idx:idx+c]
    c2=depth[i]
    c1.sort()
    c2.sort()
    if c1!=c2:
        flag=1
        break
    idx+=c

if flag==1:
    print(0)
else:
    print(1)