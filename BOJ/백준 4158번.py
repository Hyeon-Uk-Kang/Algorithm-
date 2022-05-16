import sys
while True:

    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    d={}
    for i in range(n):
        x=int(sys.stdin.readline())
        d[x]=1
    cnt=0
    for i in range(m):
        x=int(sys.stdin.readline())
        if x not in d:
            d[x]=1
        else:
            cnt+=1
    print(cnt)