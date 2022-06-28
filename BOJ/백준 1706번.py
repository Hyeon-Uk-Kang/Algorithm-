n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(input()))
v=[]
for i in range(n):
    temp=""
    for j in range(m):
        if arr[i][j]!='#':
            temp+=arr[i][j]
        elif len(temp)>=2:
            v.append(temp)
            temp=""
        else:
            temp=""
    if len(temp)>=2:
        v.append(temp)

for i in range(m):
    temp=""
    for j in range(n):
        if arr[j][i]!='#':
            temp+=arr[j][i]
        elif len(temp)>=2:
            v.append(temp)
            temp=""
        else:
            temp=""
    if len(temp)>=2:
        v.append(temp)
v.sort()
print(v[0])