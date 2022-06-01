tc=int(input())

while tc>0:
    n=int(input())
    arr=list(map(int,input().split()))

    sum=[0]*(n+1)
    ans=-1000000000000000
    for i in range(1,n+1):
        sum[i]=max(sum[i-1]+arr[i-1],arr[i-1])
        ans=max(ans,sum[i])

    print(ans)

    tc-=1