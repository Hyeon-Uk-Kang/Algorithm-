import sys

tc = int(input())
while tc > 0:
    s = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    r, f, b = 0, 0, 0

    for i in s:
        if i == 'R':
            r += 1
        else:
            if r % 2 == 0:
                f += 1
            else:
                b += 1

    if f + b <= n:
        arr = arr[f:n - b]
        if r%2==0:
            print("["+','.join(arr)+"]")
        else:
            print("["+','.join(arr[::-1])+"]")
    else:
        print("error")

    tc -= 1