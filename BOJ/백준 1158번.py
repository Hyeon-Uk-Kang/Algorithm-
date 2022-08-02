from collections import deque
n,m=map(int,input().split())

q=deque()

for i in range(1,n+1):
    q.append(i)

arr=[]
while q:

    for i in range(m-1):
        q.append(q[0])
        q.popleft()

    x=q.popleft()
    arr.append(x)

print("<",end="")
for i in range(len(arr)-1):
    print(arr[i],end="")
    print(",",end=" ")

print(arr[-1],end="")
print(">")