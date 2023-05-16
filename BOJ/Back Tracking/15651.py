import sys

input = sys.stdin.readline


def dfs(lev):
    if lev == M + 1:
        print(" ".join(arr))
        return

    for i in range(1, N + 1):
        arr.append(str(i))
        dfs(lev + 1)
        arr.pop()


N, M = map(int, input().split())
arr = []
dfs(1)
