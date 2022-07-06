a=input()
v=[]
for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            t=a[:j][::-1]+a[j:k][::-1]+a[k:][::-1]
            v.append(t)

v.sort()
print(v[0])