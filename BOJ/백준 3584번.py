tc=int(input())

while tc>0:
    n=int(input())
    visit=[0]*(n+1)
    p=[i for i in range(n+1)]
    arr=[[] for i in range(n+1)]

    for i in range(n-1):
        a,b=map(int,input().split())
        p[b]=a

    x,y=map(int,input().split())
    visit[x]=1

    while x!=p[x]:
        x=p[x]
        visit[x]=1

    while True:
        if visit[y]==1:
            print(y)
            break
        y=p[y]

    tc-=1