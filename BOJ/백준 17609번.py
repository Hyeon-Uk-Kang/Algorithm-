n=int(input())

def f(a):
    left = 0
    right = len(a) - 1
    while left < right:
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1:
                tmp = a[:right] + a[right + 1:]
                if tmp==tmp[::-1]:
                    return 1
            if left+1<right:
                tmp=a[:left]+a[left+1:]
                if tmp==tmp[::-1]:
                    return 1
            return 2

    return 0
for i in range(n):
    a=input()
    print(f(a))
