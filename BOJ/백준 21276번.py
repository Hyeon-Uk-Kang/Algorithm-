from collections import deque

n=int(input())
arr=list(input().split())
arr.sort()

name={}
number={}
for i in range(n):
    number[arr[i]]=i+1
    name[i+1]=arr[i]

m=int(input())
data=[[] for i in range(n+1)]
indegree=[0]*(n+1)

for i in range(m):
    x,y=list(input().split())
    data[number[y]].append(number[x])
    indegree[number[x]]+=1

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

print(len(q))
for i in q:
    print(name[i],end=" ")
print()

son=[[] for i in range(n+1)]
while q:
    now=q.popleft()
    for i in data[now]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
            son[now].append(i)

for i in range(n):
    print(arr[i],end=" ")
    print(len(son[i+1]),end=" ")
    son[i+1].sort()
    for k in son[i+1]:
        print(name[k],end=" ")
    print()

