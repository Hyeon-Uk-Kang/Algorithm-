import heapq
n,m=map(int,input().split())
arr=[]
bag=[]
for i in range(n):
    x,y=map(int,input().split())
    heapq.heappush(arr,(x,y))

for i in range(m):
    x=int(input())
    bag.append(x)


bag.sort()
q=[]
ans=0
for i in bag:
    while arr and i>=arr[0][0]:
        w,v=heapq.heappop(arr)
        heapq.heappush(q,-v)

    if q:
        x=-heapq.heappop(q)
        ans+=x
    elif not arr:
        break
print(ans)