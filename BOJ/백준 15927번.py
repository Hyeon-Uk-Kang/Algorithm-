a=input()

n=len(a)

def f(a,left,right):
    while left<right:
        if a[left]!=a[right]:
            return 0
        left+=1
        right-=1
    return 1
if f(a,0,n-1)==0:
    print(n)
elif f(a,0,n-2)==0:
    print(n-1)
else:
    print(-1)