import sys, copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(n)]
matrix_2 = copy.deepcopy(matrix)

queue1 = deque()  # 불이 번지는 queue
queue2 = deque()  # 지훈이가 움직이는 queue

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "F":
            queue1.append((i, j, 0))  # 불이 붙은 곳이 여러 곳일 수 있으므로 time도 함께 넣어주기

        elif matrix[i][j] == "J":
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:  # 만약 처음부터 지훈이가 가장자리에 위치한다면 그냥 탈출
                print(1)
                exit()
            queue2.append((i, j, 0))  # 지훈이는 그냥 넣어주기...

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 불이 번지는 queue 구하기

while queue1:
    loc_x, loc_y, time = queue1.popleft()

    time += 1
    for index in range(4):
        nx = loc_x + dx[index]
        ny = loc_y + dy[index]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if matrix[nx][ny] == ".":
            matrix[nx][ny] = time
            queue1.append((nx, ny, time))

min_value = sys.maxsize
chk = False

while queue2:
    loc_x, loc_y, time = queue2.popleft()

    time += 1
    for index in range(4):
        nx = loc_x + dx[index]
        ny = loc_y + dy[index]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            print(time)
            exit()

        if matrix_2[nx][ny] == "." and time < matrix[nx][ny]:
            matrix_2[nx][ny] = time
            queue2.append((nx, ny, time))

            # if nx == n - 1 or nx == 0 or ny == m - 1 or ny == 0:
            #     chk = True
            #     min_value = min(min_value, time + 1)

if chk:
    print(min_value)
else:
    print("IMPOSSIBLE")
