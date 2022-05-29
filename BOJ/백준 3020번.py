n,h=map(int,input().split())

down=[0]*(h+1)
up=[0]*(h+1)

cnt=n

for i in range(n):
    if i%2==0:
        x=int(input())
        down[x]+=1
    else:
        x=int(input())
        up[x]+=1

for i in range(h-1,0,-1):
    down[i]+=down[i+1]
    up[i]+=up[i+1]

ans=0
for i in range(1,h+1):
    if cnt>(down[i]+up[h-i+1]):
        cnt=(down[i]+up[h-i+1])
        ans=1
    elif cnt==(down[i]+up[h-i+1]):
        ans+=1

print(cnt,ans)