import sys

input = sys.stdin.readline
import heapq


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n)]
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a - 1) != find_parent(parent, b - 1):
        union_parent(parent, a - 1, b - 1)
        cnt += 1

costs = [list(map(int, input().split())) for _ in range(n)]
kruskal = []

if cnt == n - 1:
    print(0, 0)
else:
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if find_parent(parent, i) != find_parent(parent, j):
                heapq.heappush(kruskal, [costs[i][j], i, j])

    connected = []
    total = 0

    while kruskal:
        cost, x, y = heapq.heappop(kruskal)

        if find_parent(parent, x) == find_parent(parent, y):
            continue

        cnt += 1
        union_parent(parent, x, y)
        total += cost
        connected.append([x + 1, y + 1])
        if cnt == n - 1:
            break

    print(total, len(connected))
    for point in connected:
        print(*point)