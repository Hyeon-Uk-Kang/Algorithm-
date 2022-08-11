while True:
    n=int(input())
    if n==-1:
        break

    v=[]
    for i in range(1,n):
        if n%i==0:
            v.append(i)

    if sum(v)==n:
        print(n,end=" ")
        print("=",end=" ")
        for i in range(len(v)-1):
            print(v[i],end=" ")
            print("+",end=" ")
        print(v[-1])
    else:
        print(n,end=" ")
        print("is NOT perfect.")
    #print()