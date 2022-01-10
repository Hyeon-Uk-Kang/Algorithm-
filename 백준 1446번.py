import sys

n,d=map(int,sys.stdin.readline().split())
arr=[[] for i in range(d+1)]

for i in range(n):
    s,e,w=map(int,sys.stdin.readline().split())
    arr[s].append((e,w))

dist=[i for i in range(d+1)]

for i in range(d+1):
    if i!=0:
        dist[i]=min(dist[i],dist[i-1]+1)
    for e,w in arr[i]:
        if e<=d and dist[e]>=w+dist[i]:
            dist[e]=w+dist[i]

print(dist[d])