import sys

n,m=map(int,sys.stdin.readline().split())
parent=[i for i in range(n+1)]
num=[1]*(n+1)

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

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    unite(a,b)

ctp,hansol,k=map(int,sys.stdin.readline().split())

ctp_num=find(ctp)
hansol_num=find(hansol)

v=[]
for i in range(1,n+1):
    if parent[i]!=i:
        continue
    x=find(i)

    if x==ctp_num or x==hansol_num:
        continue

    v.append(num[x])

v.sort(reverse=True)

for i in range(k):
    num[ctp_num]+=v[i]

print(num[ctp_num])

