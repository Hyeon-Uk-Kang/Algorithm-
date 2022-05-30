import sys
n=int(input())
arr=[0]+list(map(int,input().split()))
m=int(input())

sum=[0]*(n+1)

for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i]

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    print(sum[b]-sum[a-1])