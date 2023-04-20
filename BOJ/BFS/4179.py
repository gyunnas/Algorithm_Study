import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(n)]

queue1 = deque()  # 불이 번지는 queue
queue2 = deque()  # 지훈이가 움직이는 queue

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "F":
            queue1.append((i, j))

        elif matrix[i][j] == "J":
            queue2.append((i, j))

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 불이 번지는 queue 구하기
time = 0
while queue1:
    loc_x, loc_y = queue1.popleft()
    time += 1
    for index in range(4):
        nx = loc_x + dx[index]
        ny = loc_y + dy[index]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if matrix[nx][ny] == ".":
            matrix[nx][ny] = time
            queue1.append((nx, ny))

time = 0
while queue2:
    loc_x, loc_y = queue2.popleft()
    time += 1
    for index in range(4):
        nx = loc_x + dx[index]
        ny = loc_y + dy[index]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if matrix[nx][ny] and matrix[nx][ny] > time and matrix[nx][ny] != -1:
            matrix[nx][ny] = time
            matrix[loc_x][loc_y] = -1
            queue2.append((nx, ny))

print(matrix)
