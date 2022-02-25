import sys

input = sys.stdin.readline

n, p = map(int, input().rstrip().split())
arrival_costs = [int(input().rstrip()) for _ in range(n)]

edges = []
for _ in range(p):
    a, b, cost = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    edges.append((a, b, cost * 2 + arrival_costs[a] + arrival_costs[b]))

parent = list(range(n))
rank = [0] * n


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

min_total_cost += min(arrival_costs)

print(min_total_cost)