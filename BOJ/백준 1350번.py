import sys

a=input()

if a=='1':
    print("NO")
else:
    sum1 = 1
    for i in range(len(a)):
        sum1 *= int(a[i])
        # print("sum1=",sum1)
        sum2 = 1
        for j in range(i + 1, len(a)):
            sum2 *= int(a[j])
        # print("sum2=",sum2)

        if sum1 == sum2:
            print("YES")
            exit()
    print("NO")


