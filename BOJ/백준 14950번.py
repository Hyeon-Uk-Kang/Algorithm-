import sys

input = sys.stdin.readline

n, m, t = map(int, input().rstrip().split())
edges = [tuple(map(int, input().rstrip().split())) for _ in range(m)]

parent = list(range(n + 1))
rank = [0] * (n + 1)


def find(v):
    if v == parent[v]:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]


def union(a, b):
    if rank[a] >= rank[b]:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
    else:
        parent[a] = b


edges.sort(key=lambda x: x[2])
min_total_cost = 0
for edge in edges:
    a = find(edge[0])
    b = find(edge[1])
    if a != b:
        union(a, b)
        min_total_cost += edge[2]

if n - 2 >= 1:
    n -= 2
    min_total_cost += t * (n * (n + 1)) // 2

print(min_total_cost)