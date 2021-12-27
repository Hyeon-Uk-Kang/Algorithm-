import sys

n,m=map(int,sys.stdin.readline().split())
truth=list(map(int,sys.stdin.readline().split()))
parent=[i for i in range(n+1)]
ans=m

arr=[[] for i in range(m+1)]
for i in range(1,m+1):
    data=list(map(int,sys.stdin.readline().split()))
    if data[0]>1:
        for j in range(1,len(data)):
            arr[i].append(data[j])
    elif data[0]==1:
        arr[i].append(data[1])

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])

    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a!=b:
        parent[b]=a

for i in range(1,m+1):
    n1=arr[i][0]
    for j in range(1,len(arr[i])):
        union(n1,arr[i][j])

for k in range(1,m+1):
    flag=0
    for i in range(len(arr[k])):
        for j in range(1,len(truth)):
            if find(arr[k][i])==find(truth[j]):
                flag=1
                break
        if flag==1:
            break
    if flag==1:
        ans-=1

print(ans)
