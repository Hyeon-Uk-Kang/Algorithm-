from collections import deque
tc=int(input())
while tc>0:
    s=input()
    n=int(input())
    arr=input()[1:-1].split(',')
    q=deque(arr)

    if n==0:
        q=deque()
        f,b=0,0
    r=0
    flag=0
    #print(q)
    for i in s:
        if i=='R':
            r+=1
        else:
            if len(q) == 0:
                flag = 1
                print("error")
                break
            else:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if flag==0:
        if r%2==0:
            print("["+",".join(q)+']')
        else:
            q.reverse()
            print("["+",".join(q)+']')

    tc-=1
