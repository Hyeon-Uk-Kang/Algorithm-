import sys

str=input()
cnt=[0]*26

for i in str:
    cnt[ord(i)-65]+=1

odd=0
odd_alpha=''
alpha=''

for i in range(26):
    if cnt[i]%2==1:
        odd+=1
        odd_alpha=chr(i+65)
    alpha+=chr(i+65)*(cnt[i]//2)

if odd>1:
    print("I'm Sorry Hansoo")
else:
    print(alpha+odd_alpha+alpha[::-1])