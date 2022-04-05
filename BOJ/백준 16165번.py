n,m=map(int,input().split())
d={}
number={}
while n>0:
    a=input()
    d[a]=[]

    member=int(input())
    for i in range(member):
        x=input()
        d[a].append(x)
        number[x]=a
    d[a].sort()
    n-=1

for i in range(m):
    x=input()
    a=int(input())
    if a==1:
        print(number[x])
    else:
        for i in d[x]:
            print(i)
#print(d)