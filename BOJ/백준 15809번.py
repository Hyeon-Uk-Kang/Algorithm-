import sys

n,m=map(int,sys.stdin.readline().split())
power=[0]
parent=[i for i in range(n+1)]
for i in range(n):
    x=int(input())
    power.append(x)

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def unite(a,b):
    a=find(a)
    b=find(b)

    if b>a:
        parent[b]=a
        power[a]+=power[b]
        power[b]=0
    else:
        parent[a]=b
        power[b]+=power[a]
        power[a]=0

for i in range(m):
    num,a,b=map(int,sys.stdin.readline().split())
    if num==1:
        unite(a,b)
    else:
        a=find(a)
        b=find(b)
        if power[a] > power[b]:
            power[a] -= power[b]
            power[b] = 0
            parent[b] = a
        elif power[b] > power[a]:
            power[b] -= power[a]
            power[a] = 0
            parent[a] = b
        else:
            parent[a] = 0
            parent[b] = 0

cnt=0
v=[]
for i in range(1,n+1):
    if power[i]!=0:
        cnt+=1
        v.append(power[i])

v.sort()
print(cnt)
for i in range(len(v)):
    print(v[i],end=" ")
