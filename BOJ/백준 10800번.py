n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append((b,a,i))

arr.sort()

sum=0
color=[0]*(n+1)
s=[0]*2001
ans=[0]*n

for i in range(n):
    w=arr[i][0]
    c=arr[i][1]
    idx=arr[i][2]

    sum+=w
    color[c]+=w
    s[w]+=w

    ans[idx]=sum-color[c]-s[w]+w
    if i!=0 and w==arr[i-1][0] and c==arr[i-1][1]:
        ans[idx]=ans[arr[i-1][2]]

for i in range(n):
    print(ans[i])

