import sys
import copy
from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

n=int(input())
arr=[]
v=[]
t=[]
select=[0]*36
for i in range(n):
    arr.append(list(input().split()))
    for j in range(n):
        if arr[i][j]=='X':
            v.append((i,j))
        elif arr[i][j]=='T':
            t.append((i,j))

arr2=[[0]*n for i in range(n)]

def check():
    for k in range(len(t)):
        x=t[k][0]
        y=t[k][1]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            while 0 <= nx < n and 0 <= ny < n:
                if arr2[nx][ny] == 'S':
                    return False
                elif arr2[nx][ny]=='O':
                    break
                nx += dx[i]
                ny += dy[i]

    return True

def count(idx,cnt):
    if cnt==3:
        for i in range(n):
            for j in range(n):
                arr2[i][j]=arr[i][j]
        for i in range(len(v)):
            if select[i]==1:
                x=v[i][0]
                y=v[i][1]
                arr2[x][y]='O'

        if check()==True:
            print("YES")
            exit()
        return

    for i in range(len(v)):
        if select[i]==1:
            continue
        select[i]=1
        count(i+1,cnt+1)
        select[i]=0

count(0,0)
print("NO")