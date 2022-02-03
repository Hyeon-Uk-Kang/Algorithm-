import sys
INF=sys.maxsize
n=int(input())
arr=[]
select=[0]*n
v=[]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    v.append(i)

ans=INF

def count(idx,cnt):
    global ans
    if cnt==n//2:
        sum1, sum2 = 0, 0
        t, z = [], []
        for i in range(len(v)):
            if select[i]==1:
                t.append(i)
            else:
                z.append(i)
        for i in range(len(t)):
            for j in range(len(t)):
                if i==j:
                    continue
                sum1+=arr[t[i]][t[j]]
        for i in range(len(z)):
            for j in range(len(z)):
                if i==j:
                    continue
                sum2+=arr[z[i]][z[j]]
        ans=min(ans,abs(sum1-sum2))
        if ans==0:
            print(0)
            exit(0)
        return

    for i in range(idx,len(v)):
        if select[i]==1:
            continue
        select[i]=1
        count(i+1,cnt+1)
        select[i]=0

count(0,0)
print(ans)