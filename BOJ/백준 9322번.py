tc=int(input())

while tc>0:
    n=int(input())
    arr=[]
    for i in range(3):
        a=input().split()
        arr.append(a)

    num=[]
    for i in range(n):
        num.append(arr[1].index(arr[0][i]))

    for i in num:
        print(arr[2][i],end=" ")
    tc-=1