import sys
from heapq import heappush, heappop


def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


n = int(sys.stdin.readline())
coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [0] * n
res = 0
adj = []
new = 0
visit[0] = 1
for _ in range(n - 1):
    for j in range(n):
        if visit[j] == 0:
            heappush(adj, (dist(coord[new], coord[j]), j))

    while True:
        if len(adj) == 0:
            print(-1)
            exit()

        (d, new) = heappop(adj)
        if visit[new] == 0:
            visit[new] = 1
            res = max(res, d)
            break

print(res)