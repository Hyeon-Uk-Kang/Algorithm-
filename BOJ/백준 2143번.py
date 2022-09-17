t=int(input())
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

d={}
d2={}

for i in range(n):
    s=0
    for j in range(i,n):
        s+=arr[j]
        if not s in d:
            d[s]=1
        else:
            d[s]+=1

for i in range(m):
    s=0
    for j in range(i,m):
        s+=arr2[j]
        if not s in d2:
            d2[s]=1
        else:
            d2[s]+=1

ans=0
d[0]=0
d2[0]=0
d[sum(arr)]=1
d2[sum(arr2)]=1
#print(d)
#print(d2)
for i in range(-1000000000,1000000001):
    if i in d and t-i in d2:
        #print(i,d[i],d[t-i],d[i]*d2[t-i])
        ans+=d[i]*d2[t-i]

print(ans)