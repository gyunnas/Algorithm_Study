from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 시작점이 여러 개인 BFS를 도는 방법 -> 모든 시작점을 queue에 넣어라
queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while queue:
    loc_x, loc_y = queue.popleft()

    for index in range(4):
        nx = loc_x + dx[index]
        ny = loc_y + dy[index]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if arr[nx][ny] == 0:
            arr[nx][ny] = arr[loc_x][loc_y] + 1
            queue.append((nx, ny))

value = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit()

        else:
            value = max(value, arr[i][j])

print(value - 1)
