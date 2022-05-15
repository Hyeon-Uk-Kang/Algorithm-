import bisect
tc=int(input())

while tc>0:
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    data=list(map(int,input().split()))
    data.sort()

    cnt=0
    for i in arr:
        cnt+=(bisect.bisect_left(data,i))

    print(cnt)

    tc-=1