n=int(input())
a=input()
ans=0
for i in range(len(a)):
    ans+=ord(a[i])-64
print(ans)