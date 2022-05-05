n,m,k=map(int,input().split())

arr=[[0]*101 for i in range(101)]

for i in range(1,4):
    data=list(map(int,input().split()))
    for j in range(1,4):
        arr[i][j]=data[j-1]

'''for i in range(1,4):
    for j in range(1,4):
        print(arr[i][j],end=" ")
    print()'''
time=0
hang=3
yul=3
while True:
    if arr[n][m]==k:
        print(time)
        break
    if time==100:
        print(-1)
        break

    size=[]
    if hang>=yul:

        for i in range(1,hang+1):
            v=[]
            num=[0]*101
            for j in range(1,yul+1):
                num[arr[i][j]]+=1

            for j in range(1,101):
                if num[j]!=0:
                    v.append((num[j],j))

            v.sort()
            for j in range(1,yul+1):
                arr[i][j]=0

            idx=1
            for j in v:
                arr[i][idx]=j[1]
                idx+=1
                arr[i][idx]=j[0]
                idx+=1

            idx-=1
            size.append(idx)
        size.sort()
        yul=size[-1]
    else:

        for i in range(1,yul+1):
            v=[]
            num=[0]*101
            for j in range(1,hang+1):
                num[arr[j][i]]+=1

            for j in range(1,101):
                if num[j]!=0:
                    v.append((num[j],j))

            v.sort()
            for j in range(1,hang+1):
                arr[j][i]=0

            idx=1
            for j in v:
                arr[idx][i]=j[1]
                idx+=1
                arr[idx][i]=j[0]
                idx+=1

            idx-=1
            size.append(idx)
        size.sort()
        hang=size[-1]

    time+=1





