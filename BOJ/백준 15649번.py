n, m = map(int, input().split())

s = [0] * (n + 1)
arr = [0] * (n + 1)


def dfs(cnt):
    if cnt == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1, n + 1):
        if s[i] == 0:
            s[i] = 1
            arr[cnt] = i
            dfs(cnt + 1)
            s[i] = 0


dfs(0)