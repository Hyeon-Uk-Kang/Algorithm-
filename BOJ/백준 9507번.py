

arr=[0]*70

arr[0]=1
arr[1]=1
arr[2]=2
arr[3]=4
for i in range(4,70):
    arr[i]=arr[i-1]+arr[i-2]+arr[i-3]+arr[i-4]

n=int(input())
for i in range(n):
    x=int(input())
    print(arr[x])