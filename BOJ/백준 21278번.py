import sys

INF=sys.maxsize
n,m=map(int,sys.stdin.readline().split())
arr=[[INF]*(n+1) for i in range(n+1)]
select=[0]*(n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            arr[i][j]=0

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a][b]=1
    arr[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]>arr[i][k]+arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

v=[]
ans=INF
for i in range(1,n+1):
    v.append(i)

def count(idx,cnt):
    global ans,index1,index2
    if cnt==2:
        sum=0
        res=[]
        d=[]
        for i in range(len(v)):
            if select[i]==1:
                res.append(i+1)
            else:
                d.append(i+1)

        for i in d:
            sum+=min(arr[i][res[0]],arr[i][res[1]])
        if ans>sum:
            ans=sum
            index1=res[0]
            index2=res[1]
        return

    for i in range(idx,len(v)):
        if select[i]==1:
            continue
        select[i]=1
        count(i+1,cnt+1)
        select[i]=0

count(0,0)
print(index1,index2,ans*2)