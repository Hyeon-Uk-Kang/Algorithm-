n=int(input())

arr=list(map(int,input().split()))
ans=0
for i in range(n-1):
    cnt=0
    for j in range(i+1,n):
        if arr[j]<arr[i]:
            cnt+=1
        elif arr[j]>arr[i]:
            ans=max(ans,cnt)
            break
    ans=max(ans,cnt)
print(ans)