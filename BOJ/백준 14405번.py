a=input()

a2=a.replace('pi','1')
a3=a2.replace('ka','1')
a4=a3.replace('chu','1')

flag=0
for i in a4:
    if i!='1':
        flag=1
        break

if flag==1:
    print("NO")
else:
    print("YES")