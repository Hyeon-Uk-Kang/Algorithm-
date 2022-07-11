n,m=map(int,input().split())
arr=list(map(int,input().split()))
cnt=[0]*m
sum=[0]*(n+1)

for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i-1]
    cnt[sum[i]%m]+=1

ans=0
print(cnt)
for i in range(m):
    ans+=(cnt[i]*(cnt[i]-1))//2
    print(ans)
#print(ans)