import sys

t=int(input())

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)

    if a!=b:
        parent[b]=a
        cnt[a]+=cnt[b]
for i in range(t):
    n=int(input())
    cnt = {}
    parent = {}


    for i in range(n):
        f1,f2=sys.stdin.readline().split()


        if f1 not in cnt:
            cnt[f1]=1
            parent[f1]=f1
        if f2 not in cnt:
            cnt[f2]=1
            parent[f2]=f2

        union(f1,f2)
        print(cnt[find(f1)])

