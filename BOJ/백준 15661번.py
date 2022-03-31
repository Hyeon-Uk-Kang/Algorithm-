n=int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

v=[]
ans=10000000000000
for i in range(n):
    v.append(i)

def dfs(idx,cnt,k):
    global ans
    if cnt==k:
        sum1,sum2=0,0
        start,link=[],[]
        for i in range(len(v)):
            if s[i]==1:
                start.append(i)
            else:
                link.append(i)

        for i in range(len(start)):
            for j in range(len(start)):
                sum1+=arr[start[i]][start[j]]

        for i in range(len(link)):
            for j in range(len(link)):
                sum2+=arr[link[i]][link[j]]
        #print(start,link)
        #print(sum1,sum2)
        ans=min(ans,abs(sum1-sum2))
        return

    for i in range(idx,len(v)):
        s[i]=1
        dfs(i+1,cnt+1,k)
        s[i]=0

for k in range(1,n//2+1):
    s=[0]*len(v)
    dfs(0,0,k)

print(ans)