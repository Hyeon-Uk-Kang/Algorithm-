import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    nodes = [[] for _ in range(n+1)]
    in_degree = [0 for _ in range(n+1)]
    rank = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(n):
        for j in range(i+1, n):
            nodes[rank[i]].append(rank[j])
            in_degree[rank[j]] += 1

    m = int(sys.stdin.readline().rstrip())

    for _ in range(m):
        tail, head = map(int, sys.stdin.readline().rstrip().split())

        if head in nodes[tail]:
            # tail -> head를 head -> tail로 바꾼다.
            nodes[tail].remove(head)
            in_degree[head] -= 1
            nodes[head].append(tail)
            in_degree[tail] += 1
        else:
            nodes[head].remove(tail)
            in_degree[tail] -= 1
            nodes[tail].append(head)
            in_degree[head] += 1

    queue = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)

    if len(queue) > 1: print('?')
    else:
        result = []
        while queue:
            cur_node = queue.popleft()
            result.append(cur_node)

            for next_node in nodes[cur_node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)

        if len(result) == n: print(*result, sep=' ')
        else: print('IMPOSSIBLE')