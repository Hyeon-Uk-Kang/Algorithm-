n,m=map(int,input().split())
arr=[0]+list(map(int,input().split()))
sum=[0]*(n+1)

for i in range(1,n+1):
    if i==1:
        sum[i]=arr[i]
    else:
        sum[i]=sum[i-1]+arr[i]

ans=-10000000000000
for i in range(m,n+1):
    ans=max(ans,sum[i]-sum[i-m])

print(ans)
