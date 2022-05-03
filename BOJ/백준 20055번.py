from collections import deque
import sys
n,k=map(int,sys.stdin.readline().split())
arr=deque(list(map(int,sys.stdin.readline().split())))
robot=deque([0]*n)
time=0

while True:
    arr.rotate(1)
    robot.rotate(1)
    robot[-1]=0

    if sum(robot):
        for i in range(n - 2, -1, -1):
            if robot[i] == 1 and robot[i + 1] == 0 and arr[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                arr[i + 1] -= 1
        if robot[-1] == 1:
            robot[-1] = 0


    if robot[0]==0 and arr[0]>=1:
        arr[0]-=1
        robot[0]=1
    time+=1
    if arr.count(0)==k:
        break

print(time)