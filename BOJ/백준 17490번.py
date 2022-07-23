n,m,k=map(int,input().split())
arr=list(map(int,input().split()))

p=[i for i in range(n+1)]
v=[0]*(n+1)
cnt=0

if m<1:
    print("YES")
    exit()
def find(x):

    if x!=p[x]:
        p[x]=find(p[x])
    return p[x]

def unite(a,b):
    a=find(a)
    b=find(b)
    if b>a:
        p[b]=a
    elif a>b:
        p[a]=b

for i in range(m):
    a,b=map(int,input().split())
    if a==n and b==1:
        v[a]=1
    elif a==1 and b==n:
        v[b]=1
    else:
        if a>b:
            v[b]=1
        else:
            v[a]=1
edge=[]
for i in range(1,n+1):
    if v[i]==0:
        if i<n:
            edge.append((0,i,i+1))
        else:
            edge.append((0, n,1))


for i in range(1,n+1):
    edge.append((arr[i-1],0,i))

edge.sort()
res=0

for i in edge:
    cost,a,b=i
    if find(a)!=find(b):
        unite(a,b)
        res+=cost
        cnt+=1

if cnt==n and k>=res:
    print("YES")
else:
    print("NO")