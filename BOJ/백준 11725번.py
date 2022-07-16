import sys
sys.setrecursionlimit(10**9)

n=int(input())
arr=[[] for i in range(n+1)]
parent=[0]*(n+1)

for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(start):
    for i in arr[start]:
        if parent[i]==0:
            parent[i]=start
            dfs(i)

dfs(1)

for i in range(2,n+1):
    print(parent[i])