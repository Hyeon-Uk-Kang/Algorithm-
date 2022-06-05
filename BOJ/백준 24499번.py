n,m=map(int,input().split())
arr=list(map(int,input().split()))

for i in range(n):
    arr.append(arr[i])
#print(arr)
n=len(arr)
#print(n)
window=sum(arr[:m])
ans=window

for i in range(m,n):
    window+=arr[i]-arr[i-m]
    #print(window)
    ans=max(ans,window)
print(ans)