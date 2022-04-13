n,m=map(int,input().split())
lesson=list(map(int,input().split()))

left=max(lesson)
right=sum(lesson)

def f():

    cnt=1
    sum=0
    for i in range(n):
        if sum+lesson[i]>mid:
            cnt+=1
            sum=0
        sum+=lesson[i]

    return cnt


while left<=right:
    mid=(left+right)//2
    res=f()
    print(mid,res)
    if res>m:
        left=mid+1
    else:
        ans=mid
        right=mid-1
print(ans)