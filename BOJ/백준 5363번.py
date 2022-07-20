n=int(input())

for i in range(n):
    a=list(input().split())
    a.append(a[0])
    a.append(a[1])
    a.pop(0)
    a.pop(0)
    for j in a:
        print(j,end=" ")
    print()