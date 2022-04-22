n=int(input())

arr=list(map(int,input().split()))
arr.sort()

m=int(input())
data=list(map(int,input().split()))


for i in data:

    start = 0
    end = n - 1
    flag=0

    while start<=end:
        mid=(start+end)//2
        if arr[mid]==i:
            flag=1
            break
        elif arr[mid]>i:
            end=mid-1
        else:
            start=mid+1

    if flag==1:
        print(1)
    else:
        print(0)
