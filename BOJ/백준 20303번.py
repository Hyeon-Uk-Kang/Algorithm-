import sys

n,m,k=map(int,sys.stdin.readline().split())
arr=[0]+list(map(int,sys.stdin.readline().split()))
parent=[i for i in range(n+1)]
num=[1]*(n+1)

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])

    return parent[x]

def unite(a,b):
    a=find(a)
    b=find(b)

    if b>a:
        parent[b]=a
        num[a]+=num[b]
        arr[a]+=arr[b]
        num[b]=0
        arr[b]=0
    elif a>b:
        parent[a]=b
        num[b]+=num[a]
        arr[b]+=arr[a]
        num[a]=0
        arr[a]=0

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    unite(a,b)

print(num)
print(arr)
dp=[[0]*(k) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k):
        if j >= num[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - num[i]] + arr[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k-1])


