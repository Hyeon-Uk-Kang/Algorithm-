n,h,w=map(int,input().split())

v=['?']*(n*w)
arr=[]
for i in range(h):
    data=input()
    for j in range(len(data)):
        if data[j]!='?':
            v[j]=data[j]

res=[]
for i in range(0,len(v),w):
    flag=0
    for j in range(i,i+w):
        if v[j]!='?':
            res.append(v[j])
            flag=1
            break
    if flag==0:
        res.append("?")
print(''.join(res))