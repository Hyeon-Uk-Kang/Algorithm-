a=input()
q=[]
s=['P','P','A','P']
for i in range(len(a)):
    q.append(a[i])
    if q[-4:]==s:
        for _ in range(3):
            q.pop()

if q==s or q==['P']:
    print("PPAP")
else:
    print("NP")