k,n,f=map(int,input().split())
fr=[[0]*(n+1) for i in range(n+1)]
num=[0]*(n+1)
for i in range(f):
    a,b=map(int,input().split())
    fr[a][b]=1
    fr[b][a]=1
    num[a]+=1
    num[b]+=1

flag=0
s=[0]*(n+1)

def check(x):

    for i in range(1,n+1):
        if s[i]==1:
            if fr[x][i]==0:
                return False
    return True

def dfs(idx,cnt):
    global flag
    print("ssssss=idx,cnt,flag",idx,cnt,flag)
    if flag==1:
        return

    if cnt==k:
        flag=1
        for i in range(1, n + 1):
            if s[i] == 1:
                print(i)
        return

    for i in range(idx+1,n+1):     #idx 줄이기해보기
        if fr[idx][i]==1:
            print("idx,i===",idx,i)
            if check(i)==True:
                s[i]=1
                dfs(i,cnt+1)
                s[i]=0
                if i==6:
                    print("sex,six",i,flag)


for i in range(1,n+1):
    if flag==1:
        break
    if num[i]>=k-1:
        s[i]=1
        dfs(i,1)
        s=[0]*(n+1)
        #s[i]=0

if flag==0:
    print(-1)


