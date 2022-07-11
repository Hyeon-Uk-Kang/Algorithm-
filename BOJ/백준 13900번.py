n=int(input())
arr=[0]+list(map(int,input().split()))
sum=[0]*(n+1)
for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i]

ans=0
for i in range(1,n+1):
    ans+=arr[i]*(sum[n]-sum[i])
print(ans)