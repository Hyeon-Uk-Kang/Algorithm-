import sys
import copy
INF=int(1e9)

n=int(input())
arr=[[0]*(n+1)]

for i in range(1,n+1):
    arr.append([0]+list(map(int,sys.stdin.readline().split())))
arr2=copy.deepcopy(arr)

flag=0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if k==i or k==j:
                continue
            elif arr[i][j]==arr[i][k]+arr[k][j]:
                arr2[i][j]=INF
            elif arr[i][j]>arr[i][k]+arr[k][j]:
                flag=1

if flag==1:
    print(-1)
else:
    sum=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr2[i][j]==INF:
                continue
            sum+=arr2[i][j]

    print(sum//2)