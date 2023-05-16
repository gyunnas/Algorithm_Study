import sys

input = sys.stdin.readline


def adjacent(x, y):
    # 열이 같거나 대각선에 위치해 있으면 return False
    if x == 0: return True
    if chess[x-1][y] == 1: return False
    if y>0:
        if abs(chess[x][y] - )


def dfs(level):  # level: 몇 번째 줄
    global ans, N

    if level == N:
        ans += 1
        return

    for index in range(N):  # 몇 번째 칸
        if adjacent(level, index):
            chess[level][index] = 1
            dfs(level + 1)
            chess[level][index] = 0
    pass


N = int(input())
chess = [[0] * N for _ in range(N)]

print(chess)
ans = 0
dfs(0)
