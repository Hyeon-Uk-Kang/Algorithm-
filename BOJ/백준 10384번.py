tc=int(input())
n=1
while tc>0:
    alpha=[0]*26
    a=input()
    a=a.lower()
    for i in range(len(a)):
        if a[i].islower():
            alpha[ord(a[i])-97]+=1
    print("Case ",end="")
    print(n,end="")
    print(":",end=" ")
    if min(alpha)==0:
        print("Not a pangram")
    elif min(alpha)==1:
        print("Pangram!")
    elif min(alpha)==2:
        print("Double pangram!!")
    elif min(alpha)==3:
        print("Triple pangram!!!")
    #print(alpha)
    tc-=1
    n+=1