import sys

n=int(input())
parent=[i for i in range(1000001)]
num=[1]*(1000001)

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def unite(a,b):
    a=find(a)
    b=find(b)

    if b>a:
        parent[b]=a
        num[a]+=num[b]
        num[b]=0
    elif a>b:
        parent[a]=b
        num[b]+=num[a]
        num[a]=0

for i in range(n):
    data=list(sys.stdin.readline().split())
    if data[0]=='I':
        a=int(data[1])
        b=int(data[2])
        if find(a)!=find(b):
            unite(a,b)
    else:
        print(num[find(int(data[1]))])
