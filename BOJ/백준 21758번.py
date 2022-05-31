n=int(input())
arr=[0]+list(map(int,input().split()))
sum=[0]*(n+1)

for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i]

#벌벌통 순서일 경우

ans=-10000000000000000
for i in range(2,n):
    ans=max(ans,sum[n]-arr[1]-arr[i]+(sum[n]-sum[i]))

#통벌벌
for i in range(2,n):
    ans=max(ans,sum[n]-arr[i]-arr[n]+sum[i-1])

#벌통벌
for i in range(2,n):
    ans=max(ans,sum[i]-arr[1]+sum[n]-sum[i-1]-arr[n])

print(ans)