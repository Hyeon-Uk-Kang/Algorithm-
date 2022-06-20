n,m=map(int,input().split())
w=input()
s=input()
wl=[0]*52
sl=[0]*52

for i in range(n):
    if 'a'<=w[i]<='z':
        wl[ord(w[i])-ord('a')]+=1
    else:
        wl[ord(w[i])-ord('A')+26]+=1

st,length,cnt=0,0,0

for i in range(m):
    if 'a'<=s[i]<='z':
        sl[ord(s[i])-ord('a')]+=1
    else:
        sl[ord(s[i]) - ord('A')+26] += 1
    length+=1

    if length==n:
        if wl==sl:
            cnt+=1
        if 'a'<=s[st]<='z':
            sl[ord(s[st])-ord('a')]-=1
        else:
            sl[ord(s[st]) - ord('A')+26] -= 1
        st+=1
        length-=1
print(cnt)