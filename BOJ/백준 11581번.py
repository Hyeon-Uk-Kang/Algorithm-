n=int(input())
visit=[0]*(n+1)
arr=[[] for i in range(n+1)]
for i in range(1,n):
    x=int(input())
    data=list(map(int,input().split()))
    for j in data:
        arr[i].append(j)

def dfs(start):
    if visit[start]==1:
        print("CYCLE")
        exit()
    visit[start]=1
    for i in arr[start]:
        if visit[i]!=2:
            dfs(i)
    visit[start]=2


dfs(1)
print("NO CYCLE")