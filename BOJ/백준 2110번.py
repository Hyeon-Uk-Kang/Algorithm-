import sys

n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)

arr.sort()

start=1
end=arr[-1]-arr[0]

while start<=end:

    mid=(start+end)//2
    cnt=1
    cur=arr[0]
    for i in range(n):
        if mid+cur<=arr[i]:
            cnt+=1
            cur=arr[i]

    if cnt>=m:
        start=mid+1
        ans=mid
    else:
        end=mid-1
print(ans)