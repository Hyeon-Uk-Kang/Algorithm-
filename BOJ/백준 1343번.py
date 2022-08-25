a=input()

a=a.replace("XXXX",'AAAAA')
a=a.replace("XX","BB")

if 'X' in a:
    print(-1)
else:
    print(a)