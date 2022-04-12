a=input()
b=list(input())

q=[]
for i in range(len(a)):
    q.append(a[i])
    if q[-len(b):]==b:
        for i in range(len(b)):
            q.pop()

if len(q)==0:
    print("FRULA")
else:
    print(''.join(q))