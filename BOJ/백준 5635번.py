n=int(input())
arr=[]
for i in range(n):
    a,b,c,d=input().split()
    b=int(b)
    c=int(c)
    d=int(d)
    arr.append((a,b,c,d))

arr.sort(key=lambda x:(x[3],x[2],x[1]))
print(arr[n-1][0])
print(arr[0][0])