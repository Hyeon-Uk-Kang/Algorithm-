n,t=map(int,input().split())
arr=[0]+list(map(int,input().split()))
ans=0
res=[]
def dfs(m,idx,cnt):
    global ans
    if cnt==m:
        sum=0
        for i in range(1,n+1):
            if s[i]==1:
                sum+=arr[i]

        if sum==t:
            ans+=1
        return

    for i in range(idx,n+1):
        if s[i]==0:
            s[i]=1
            dfs(m,i+1,cnt+1)
            s[i]=0
for i in range(1,n+1):
    s=[0]*(n+1)
    dfs(i,1,0)
print(ans)