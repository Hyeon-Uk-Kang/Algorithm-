import sys

n,m=map(int,sys.stdin.readline().split())
d={}

for i in range(n):
    s=input()
    d[s]=s

def find(x):
    if d[x]!=x:
        d[x]=find(d[x])

    return d[x]

def union(x,y):
    a=find(x)
    b=find(y)

    if a!=b:
        d[y]=x
    else:
        d[x]=x
        d[y]=x

for i in range(m):
    s=input().split(',')
    if s[2]=='1':
        union(s[0],s[1])
    else:
        union(s[1],s[0])

ans=set()
for i in d.values():
    ans.add(find(i))

print(len(ans))
ans=list(ans)
ans.sort()

for i in ans:
    print(i)