n=int(input())

arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)

arr2=sorted(arr)

ans=0
for i in range(1,n+1):
    ans+=abs(arr2[i-1]-i)

print(ans)