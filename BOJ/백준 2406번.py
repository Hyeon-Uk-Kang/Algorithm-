n,m=map(int,input().split())

p=[i for i in range(n+1)]

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
    unite(a,b)

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

edge=[]

for i in range(1,n-1):
    for j in range(i+1,n):
        edge.append((arr[i][j],i+1,j+1))

edge.sort()
result=0
v=[]
for i in edge:
    cost=i[0]
    a=i[1]
    b=i[2]

    if find(a)!=find(b):
        unite(a,b)
        result+=cost
        v.append((a,b))

if len(v)==0:
    print(0,0)
else:
    print(result,len(v))
    for i in v:
        print(i[0],i[1])
