n,k,m=map(int,input().split())
arr=[0]*(n+1)
for i in range(m):
    x=int(input())
    arr[x]=1

sum=[0]*(n+1)
for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i]

ans=m
for i in range(k,n+1):
    print(sum[i]-sum[i-k])
    ans=min(ans,sum[i]-sum[i-k])
print(ans)