arr=[25,10,5,1]

n=int(input())

for i in range(n):
    a=int(input())
    for j in arr:
        print(a//j,end=" ")
        a=a%j
    print()