dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
t=n**2
arr=[[] for i in range(t+1)]

for i in range(t):
    data=list(map(int,input().split()))
    for j in range(1,len(data)):
        arr[data[0]].append(data[j])

        