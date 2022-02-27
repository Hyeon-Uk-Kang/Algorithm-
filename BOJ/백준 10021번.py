import sys
from heapq import heappush, heappop


def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


n, c = map(int, sys.stdin.readline().split())
coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [0] * n
res = 0
adj = []
new = 0
visit[0] = 1
for _ in range(n - 1):
    for j in range(n):
        if visit[j] == 0:
            d = dist(coord[new], coord[j])
            if d >= c:
                heappush(adj, (d, j))

    while True:
        if len(adj) == 0:
            print(-1)
            exit()

        (d, new) = heappop(adj)
        if visit[new] == 0:
            visit[new] = 1
            res += d
            break

print(res)