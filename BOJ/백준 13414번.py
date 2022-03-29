n,m=map(int,input().split())
d={}
for i in range(m):
    a=input()
    d[a]=i

cnt=0
d=sorted(d.items(),key=lambda x:x[1])

for i,j in d:
    if cnt==n:
        break
    print(i)
    cnt+=1