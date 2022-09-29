import sys

l,k=map(int,sys.stdin.readline().split())

li=[1]*k
for i in range(2,int(k**0.5)+1):
    if li[i]==1:
        for j in range(i*2,k,i):
            li[j]=0
prime_li=[i for i in range(2,k) if li[i]==1]

good=1
for i in prime_li:
    if l%i==0:
        print("BAD",end=" ")
        print(i)
        good=0
        break
if good==1:
    print("GOOD")