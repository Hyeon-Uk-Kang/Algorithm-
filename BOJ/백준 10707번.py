arr=[]
for i in range(5):
    x=int(input())
    arr.append(x)

x=arr[0]*arr[4]

if arr[4]<=arr[2]:
    y=arr[1]
else:
    t=arr[4]-arr[2]
    y=arr[1]+t*arr[3]

print(min(x,y))