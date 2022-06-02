arr=[0]*11

for i in range(1,11):
    x=int(input())
    arr[i]=arr[i-1]+x

mmax=-100000000000000
mmin=100000000000000
for i in range(1,11):
    if 100>=arr[i]>=mmax:
        mmax=arr[i]
    if 100<=arr[i]<=mmin:
        mmin=arr[i]

a=100-mmax
b=mmin-100

if a>b:
    print(mmin)
elif b>a:
    print(mmax)
else:
    print(mmin)

