import sys

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

n,m=map(int,sys.stdin.readline().split())
edge=[]
parent=[i for i in range(n+1)]

for i in range(m+1):
    a,b,c=map(int,sys.stdin.readline().split())
    edge.append((c,a,b))

edge_up=sorted(edge)
edge_down=sorted(edge, key=lambda x:x[0], reverse=True)

cnt1,cnt2=0,0
for i in edge_up:
    num,a,b=i
    if find(a)!=find(b):
        union(a,b)
        if num==0:
            cnt1+=1

parent=[i for i in range(n+1)]
for i in edge_down:
    num,a,b=i
    if find(a)!=find(b):
        union(a,b)
        if num==0:
            cnt2+=1

print(cnt1**2-cnt2**2)

