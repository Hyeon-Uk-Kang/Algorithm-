import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

start=1
end=max(arr)
result=0
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in arr:
        if i>mid:
            cnt+=i-mid

    if cnt<m:
        end=mid-1
    else:
        start=mid+1
        result=mid
print(result)