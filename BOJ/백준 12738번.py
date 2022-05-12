import sys
import bisect
n=int(input())
arr=list(map(int,sys.stdin.readline().split()))

dp=[arr[0]]

for i in range(1,n):
    if arr[i]>dp[-1]:
        dp.append(arr[i])
    else:
        low=bisect.bisect_left(dp,arr[i])
        dp[low]=arr[i]
print(len(dp))