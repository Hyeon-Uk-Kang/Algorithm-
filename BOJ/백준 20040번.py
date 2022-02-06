import sys
sys.setrecursionlimit(10**9)
n,m=map(int,sys.stdin.readline().split())
parent=[i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

for i in range(1,m+1):
    a,b=map(int,sys.stdin.readline().split())

    if find(a)==find(b):
        print(i)
        exit()
    union(a,b)
print(0)