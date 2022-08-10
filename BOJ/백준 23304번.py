a=input()

n=len(a)
b=a[:n//2]

m=len(b)
flag=0

left=0
right=m-1
for i in range(m):
    if b[left]==b[right]:
        left+=1
        right-=1
    else:
        flag=1
        break

left=0
right=n-1
flag2=0

for i in range(n):
    if a[left]==a[right]:
        left+=1
        right-=1
    else:
        flag2=1
        break
if flag==0 and flag2==0:
    print("AKARAKA")
else:
    print("IPSELENTI")