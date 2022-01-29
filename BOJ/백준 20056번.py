import sys

n,m,k=map(int,sys.stdin.readline().split())
fireball=[]
for i in range(m):
    r,c,mi,si,di=map(int,sys.stdin.readline().split())
    fireball.append((r-1,c-1,mi,si,di))

map=[[[] for i in range(n)] for i in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while k>0:

    while fireball:
        x,y,mi,si,di=fireball.pop(0)
        nx=(x+si*dx[di])%n
        ny=(y+si*dy[di])%n
        #print(nx,ny)
        map[nx][ny].append((mi,si,di))

    for i in range(n):
        for j in range(n):
            if len(map[i][j])>=2:
                sum_m,sum_s,odd,even,cnt=0,0,0,0,len(map[i][j])
                while map[i][j]:
                    mi,si,di=map[i][j].pop(0)
                    sum_m+=mi
                    sum_s+=si
                    if di%2==0:
                        even+=1
                    else:
                        odd+=1
                if odd==cnt or even==cnt:
                    nd=[0,2,4,6]
                else:
                    nd=[1,3,5,7]
                if sum_m//5>0:
                    for zz in nd:
                        fireball.append((i,j,sum_m//5,sum_s//cnt,zz))
            if len(map[i][j])==1:
                mi,si,di=map[i][j].pop(0)
                fireball.append((i,j,mi,si,di))
    k-=1

ans=0
for i in fireball:
    ans+=i[2]
print(ans)