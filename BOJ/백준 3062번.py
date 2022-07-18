tc=int(input())

while tc>0:
    a=input()
    t=a[::-1]
    b=int(a)+int(t)
    b=list(str(b))

    left=0
    right=len(b)-1
    flag=0

    while left<right:
        if b[left]==b[right]:
            left+=1
            right-=1
        else:
            flag=1
            break

    if flag==0:
        print("YES")
    else:
        print("NO")
    tc-=1