n=int(input())
arr=list(input().split())

ans=[]
visit=[0]*10

def ff(x,y,op):
    if op=='<':
        if x>y:
            return False
    if op=='>':
        if x<y:
            return False
    return True

def f(idx,num):

    if idx==n+1:
        ans.append(num)
        return

    for i in range(10):
        if visit[i]==1:
            continue
        if idx==0 or ff(num[idx-1],str(i),arr[idx-1]):
            visit[i]=1
            f(idx+1,num+str(i))
            visit[i]=0
f(0,'')

print(ans[-1])
print(ans[0])

