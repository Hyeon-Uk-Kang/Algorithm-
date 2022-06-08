import sys
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

sum=[0]*(n+1)

for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i-1]

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    print(sum[b]-sum[a-1])