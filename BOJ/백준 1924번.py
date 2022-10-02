a,b=map(int,input().split())

day=["SUN","MON","TUE","WED","THU","FRI","SAT"]
month=[0,31,28,31,30,31,30,31,31,30,31,30,31]

tt=sum(month[:a])+b

print(day[tt%7])