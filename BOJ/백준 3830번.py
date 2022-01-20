import sys
sys.setrecursionlimit(10**9)
def find(x):

    if parent[x]!=x:
        r=find(parent[x])
        dist[x]+=dist[parent[x]]
        parent[x]=r
    return parent[x]

def unite(x,y,w):
    a=parent[x]
    b=parent[y]

    if a!=b:
        dist[b]=dist[x]+w-dist[y]
        parent[b]=a

while True:
    n,m=map(int,sys.stdin.readline().split())
    if n==0 and m==0:
        break

    parent=[i for i in range(n+1)]
    dist=[0]*(n+1)

    for i in range(m):
        data=list(sys.stdin.readline().split())
        x = int(data[1])
        y = int(data[2])
        find(x)
        find(y)
        if data[0]=='!':

            w=int(data[3])

            unite(x,y,w)
        else:
            if parent[x]!=parent[y]:
                print("UNKNOWN")
            else:
                print(dist[y]-dist[x])