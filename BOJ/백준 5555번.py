a=input()
n=int(input())

cnt=0
for i in range(n):
    t=input()
    t+=t

    if t.find(a)!=-1:
        cnt+=1
print(cnt)