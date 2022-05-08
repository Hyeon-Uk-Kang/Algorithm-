import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
m=int(input())

arr.sort()
start=1
end=arr[-1]

while start<=end:
    mid=(start+end)//2
    total=0

    for i in arr:
        if mid>=i:
            total+=i
        else:
            total+=mid

    if total<=m:
        start=mid+1
        ans=mid
    else:
        end=mid-1
print(ans)