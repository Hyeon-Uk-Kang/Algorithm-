n=int(input())

for i in range(n):
    s,word=input().split()

    #cnt=0
    cnt=s.count(word)
    r_s=s.replace(word,"")
    print(cnt+len(r_s))

