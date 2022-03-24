import sys
sys.setrecursionlimit(10**9)
def find(x):

    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

n=int(input())
parent=[i for i in range(n+1)]

for i in range(n-2):
    a,b=map(int,sys.stdin.readline().split())
    union(a,b)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            continue
        if find(i)!=find(j):
            print(i,end=" ")
            print(j)
            exit()