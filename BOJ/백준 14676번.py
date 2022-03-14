import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    indegree[Y] += 1

building = [0] * (N + 1)


def solution(cmd):
    if cmd[0] == 1:
        if indegree[cmd[1]]: return 0
        building[cmd[1]] += 1
        if building[cmd[1]] == 1:
            for n in graph[cmd[1]]:
                indegree[n] -= 1
    else:
        if building[cmd[1]] <= 0:
            return 0
        else:
            building[cmd[1]] -= 1
            if not building[cmd[1]]:
                for n in graph[cmd[1]]:
                    indegree[n] += 1
    return 1


flag = 1
for _ in range(K):
    cmd = list(map(int, input().split()))
    flag = flag & solution(cmd)

if flag:
    print('King-God-Emperor')
else:
    print('Lier!')