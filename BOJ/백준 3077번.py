n=int(input())

arr=list(input().split())
d={}
for i in range(n):
    d[arr[i]]=i

data=list(input().split())

cnt=0
for i in range(n-1):
    for j in range(i+1,n):
        if d[data[i]]<d[data[j]]:
            cnt+=1
print(cnt,end="")
print("/",end="")
print(n*(n-1)//2)