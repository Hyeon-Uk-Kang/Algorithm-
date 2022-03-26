n,m=map(int,input().split())
arr=list(map(int,input().split()))

d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

d=sorted(d.items(),key=lambda x:-x[1])


for i,j in d:
    for k in range(j):
        print(i,end=" ")