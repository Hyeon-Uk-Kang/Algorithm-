import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
m=int(input())
data=list(map(int,sys.stdin.readline().split()))
arr.sort()
def binary(i,start,end):

    while start<=end:
        mid = (start + end) // 2
        if arr[mid]==i:
            return 1
        elif arr[mid]>i:
            end=mid-1
        else:
            start=mid+1
    return 0

for i in range(m):
    index=binary(data[i],0,n-1)
    print(index,end=" ")