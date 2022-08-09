a=input()

for i in range(len(a)):
    #print(a[i:],a[i:][::-1])
    if a[i:]==a[i:][::-1]:
        print(len(a)+i)
        break