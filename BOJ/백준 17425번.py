import sys
dp=[0]*1000001
sum=[0]*1000001
for i in range(1,1000001):
    j=1
    while i*j<=1000000:
        dp[i*j]+=i
        j+=1
    sum[i]=sum[i-1]+dp[i]

tc=int(input())
while tc>0:
    n=int(sys.stdin.readline())
    print(sum[n])
    tc-=1