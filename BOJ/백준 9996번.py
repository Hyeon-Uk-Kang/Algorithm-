n=int(input())

p=input().split('*')

for i in range(n):
    a=input()
    if a[:len(p[0])]==p[0] and a[-len(p[1]):]==p[1] and len("".join(p))<=len(a):
        print("DA")
    else:
        print("NE")