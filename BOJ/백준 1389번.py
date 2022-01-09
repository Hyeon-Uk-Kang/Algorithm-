import sys
INF=int(1e9)

n,m=map(int,sys.stdin.readline().split())

arr=[[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            arr[i][j]=0

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a][b]=1
    arr[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]>arr[i][k]+arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

sum=[0]*(n+1)
ans=INF
for i in range(1,n+1):
    for j in range(1,n+1):
        sum[i]+=arr[i][j]
    if ans>sum[i]:
        ans=sum[i]
        index=i

print(index)