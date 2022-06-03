import sys
name=input().strip()
n=int(input())
arr=[[0]*26 for i in range(len(name))]

for i in range(len(name)):
    for j in range(i,len(name)):
        arr[j][ord(name[i])-97]+=1

for i in range(n):
    alp,l,r=sys.stdin.readline().split()
    l,r=int(l),int(r)

    if l>0:
        l_value=arr[l-1][ord(alp)-97]
    else:
        l_value=0
    r_value=arr[r][ord(alp)-97]
    print(r_value-l_value)
