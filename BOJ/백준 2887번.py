import sys

n=int(input())
x,y,z=[],[],[]
parent=[i for i in range(n+1)]

for i in range(n):
    a,b,c=map(int,sys.stdin.readline().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

edge=[]

for i in range(n-1):
    edge.append((x[i + 1][0] - x[i][0], x[i + 1][1], x[i][1]))
    edge.append((y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]))
    edge.append((z[i + 1][0] - z[i][0], z[i + 1][1], z[i][1]))

edge.sort()

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])

    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a!=b:
        parent[b]=a

result=0
for i in edge:
    dist,a,b=i
    if find(a)!=find(b):
        union(a,b)
        result+=dist

print(result)