from collections import deque

n, m = map(int, input().split())  # n : 행, m : 열
arr = []
dist = []  # 시작점으로부터 거리를 담은 배열

for i in range(n):
    arr.append(list(map(int, input())))
    dist.append([-1] * m)

queue = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dist[0][0] = 1  # 출발지점에서는 거리가 0
queue.append((0, 0))

while queue:
    loc_x, loc_y = queue.popleft()

    for index in range(4):
        nx = loc_x + dx[index]
        ny = loc_y + dy[index]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if arr[nx][ny] == 0:
            continue

        if arr[nx][ny] == 1 and dist[nx][ny] == -1:
            queue.append((nx, ny))
            dist[nx][ny] = dist[loc_x][loc_y] + 1

print(dist[n - 1][m - 1])
print(dist)
