while True:
    n = int(input())
    if n==0:
        break
    arr=[]
    for i in range(n):
        a=input()
        b=a.lower()
        arr.append((b,a))
    arr.sort()
    print(arr[0][1])