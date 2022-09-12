while True:
    a=input()
    if a=='end':
        break

    flag,flag2,flag3=0,0,0
    mo=['a','e','i','o','u']
    for i in a:
        if i in mo:
            flag=1

    for i in range(len(a)-2):
        if a[i] in mo and a[i+1] in mo and a[i+2] in mo:
            flag2=1
        if a[i] not in mo and a[i+1] not in mo and a[i+2] not in mo:
            flag2=1

    for i in range(len(a)-1):
        if a[i]==a[i+1] and a[i]!='e' and a[i]!='o':
            flag3=1

    print("<",end="")
    print(a,end="")
    print("> is",end=" ")
    if flag==1 and flag2==0 and flag3==0:
        print("acceptable.")
    else:
        print("not acceptable.")
