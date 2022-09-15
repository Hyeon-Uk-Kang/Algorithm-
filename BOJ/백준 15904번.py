a=input().replace(" ",'')
ans='UCPC'
idx=0
flag=0
for i in a:
    if i==ans[idx]:
        idx+=1
    if idx==4:
        flag=1
        break
if flag==1:
    print("I love UCPC")
else:
    print("I hate UCPC")