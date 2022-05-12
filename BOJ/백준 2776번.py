tc=int(input())
while tc>0:
    d={}
    n=int(input())
    data=list(map(int,input().split()))
    for i in data:
        if i not in d:
            d[i]=1

    m=int(input())
    data2=list(map(int,input().split()))
    for i in data2:
        if i in d:
            print(1)
        else:
            print(0)
    tc-=1