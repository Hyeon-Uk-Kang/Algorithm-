from collections import deque

def get_adjacentlist(s):
    tmp = list(s)
    ret = []
    for i in range(len(s)):
        tmp[i] = str(int(not int(tmp[i])))
        if "".join(tmp) in cache:
            ret.append(cache["".join(tmp)])
        tmp[i] = str(int(not int(tmp[i])))
    return ret

def bfs(s):
    visited = [0 for _ in range(N + 1)]
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        c = q.popleft()
        adjacentlist = get_adjacentlist(inp[c])
        for v in adjacentlist:
            if visited[v] == 0:
                q.append(v)
                visited[v] = 1
                backtrack[v] = c


N, K = map(int, input().split())
cache = {}
inp = [0]
backtrack = list(range(N + 1))

for i in range(N):
    tmp = input()
    cache[tmp] = i + 1
    inp.append(tmp)

bfs(1)
for _ in range(int(input())):
    e = int(input())
    ans = []
    while e != backtrack[e]:
        ans.append(e)
        e = backtrack[e]
    if e != 1:
        print(-1)
    else:
        print(1, *ans[::-1])

