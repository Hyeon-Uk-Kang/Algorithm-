from itertools import permutations
n=int(input())
k=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)

res=set()

for i in permutations(arr,k):
    res.add(''.join(list(map(str,i))))

print(len(res))