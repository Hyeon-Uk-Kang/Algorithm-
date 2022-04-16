n=int(input())

arr=list(map(int,input().split()))
arr.sort()
sum=0
for i in range(n):
    for j in range(i+1):
        sum+=arr[j]
print(sum)