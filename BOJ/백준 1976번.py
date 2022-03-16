import sys

n=int(input())
m=int(input())
parent=[i for i in range(n+1)]
arr=[]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a!=b:
        parent[b]=a

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if arr[i][j]==1:
            union(i+1,j+1)

data=list(map(int,sys.stdin.readline().split()))

flag=0
for i in range(m-1):
    if find(data[i])!=find(data[i+1]):
        flag=1
        break

if flag==1:
    print("NO")
else:
    print("YES")