n=int(input())
d=['a','e','i','o','u']

a=input()
cnt=0
for i in a:
    if i in d:
        cnt+=1
print(cnt)