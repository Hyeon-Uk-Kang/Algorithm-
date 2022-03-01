n = int(input())
li = [input() for _ in range(n)]

s = 'abcdefghijklmnopqrstuvwxyz'
s = s + s.upper()
d = {v: i for i, v in enumerate(s, 1)}

edges = []
total_length = 0
for i in range(n):
    for j in range(n):
        if li[i][j] != "0":
            total_length += d[li[i][j]]
            if i != j:
                edges.append((i, j, d[li[i][j]]))


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


parent = list(range(n))
rank = [0] * n

edges.sort(key=lambda x: x[2])

min_needed_length = 0
for edge in edges:
    a = find(edge[0])
    b = find(edge[1])

    if a != b:
        union(a, b)
        min_needed_length += edge[2]

for i in range(n):
    find(i)

if len(set(parent)) > 1:
    print(-1)
else:
    print(total_length - min_needed_length)