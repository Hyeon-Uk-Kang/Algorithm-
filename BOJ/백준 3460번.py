tc=int(input())

while tc>0:
    n=int(input())
    arr=[]
    while n>0:
       arr.append(n%2)
       n=n//2

    for i in range(len(arr)):
        if arr[i]==1:
            print(i,end=" ")
    tc-=1