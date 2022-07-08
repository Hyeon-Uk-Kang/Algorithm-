import sys

n,m=map(int,input().split())
v=[]
d={}

for i in range(n):
    #a=sys.stdin.readline()
    a=input()
    if len(a)>=m:
        if not a in d:
            d[a]=1
        else:
            d[a]+=1

for i,j in d.items():
    v.append((i,d[i],len(i)))
v.sort(key=lambda x:(-x[1],-x[2],x[0]))

for i in range(len(v)):
    print(v[i][0])
