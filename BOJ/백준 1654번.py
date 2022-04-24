import sys

n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)

arr.sort()
start=1
end=arr[-1]

while start<=end:
    mid=(start+end)//2
    total=0

    for i in arr:
        total+=i//mid

    if total>=m:
        start=mid+1
        ans=mid
    else:
        end=mid-1
print(ans)