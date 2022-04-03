n=int(input())
v=[]

for i in range(n):
    a=input().split()
    if a[0]=='add':
        if int(a[1]) not in v:
            v.append(int(a[1]))
    elif a[0]=='check':
        if int(a[1]) in v:
            print(1)
        else:
            print(0)
    elif a[0]=='remove':
        if int(a[1]) in v:
            v.remove(int(a[1]))
    elif a[0]=='toggle':
        if int(a[1]) in v:
            v.remove(int(a[1]))
        else:
            v.append(int(a[1]))
    elif a[0]=='all':
        v=[]
        for i in range(1,21):
            v.append(i)
    elif a[0]=='empty':
        v=[]


