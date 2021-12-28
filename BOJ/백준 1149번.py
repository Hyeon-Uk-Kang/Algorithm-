import sys

n=int(input())
arr=[]
dp=[[0]*3 for i in range(n)]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(3):
    dp[0][i]=arr[0][i]

for i in range(1,n):
        dp[i][0]=min(arr[i][0]+dp[i-1][1],arr[i][0]+dp[i-1][2])
        dp[i][1] = min(arr[i][1] + dp[i - 1][0], arr[i][1] + dp[i - 1][2])
        dp[i][2] = min(arr[i][2] + dp[i - 1][0], arr[i][2] + dp[i - 1][1])

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))


