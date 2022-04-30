import sys
from collections import Counter
n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
m=int(input())
data=list(map(int,sys.stdin.readline().split()))
counter=Counter(arr)

for i in data:
    print(counter[i],end=" ")