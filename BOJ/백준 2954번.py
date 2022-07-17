a=list(input())

d=['a','e','i','o','u']
i=0
while i<len(a):
    print(a[i],end="")
    if a[i] in d:
        i+=2
    i+=1

