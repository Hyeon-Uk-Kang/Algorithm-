n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(input()))
v=[]
for i in range(n):
    tmp=""
    for j in range(m):
        if arr[i][j]!='#':
            tmp+=arr[i][j]
        elif arr[i][j]=='#':
            if len(tmp)>=2:
                v.append(tmp)
            tmp=""
    if len(tmp)>=2:
        v.append(tmp)

for i in range(m):
    tmp=""
    for j in range(n):
        if arr[j][i]!='#':
            tmp+=arr[j][i]
        elif arr[j][i]=='#':
            if len(tmp)>=2:
                v.append(tmp)
            tmp=""
    if len(tmp)>=2:
        v.append(tmp)
v.sort()
print(v[0])