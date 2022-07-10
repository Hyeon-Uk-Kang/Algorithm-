n=int(input())
arr=list(map(int,input().split()))
limit=int(input())

sum=[0]*(n+1)
for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i-1]

dp=[[0]*(n+1) for i in range(4)]

for i in range(1,4):
    for j in range(i*limit,n+1):
        if i==1:
            dp[i][j]=max(dp[i][j-1],sum[j]-sum[j-limit])
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j-limit]+sum[j]-sum[j-limit])
print(dp[3][n])