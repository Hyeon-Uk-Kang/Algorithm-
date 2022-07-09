n=int(input())
d={}
cnt=0
for i in range(n):
    a=input()
    if a=="ENTER":
        for j in d.values():
            if j==1:
                cnt+=1
        d={}
    else:
        d[a]=1

for i in d.values():
    if i==1:
        cnt+=1
print(cnt)