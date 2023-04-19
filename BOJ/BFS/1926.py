from collections import deque

n, m = map(int, input().split())  # n : 행, m : 열

arr = []
flag = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    flag.append([False] * m)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()  # queue
answer = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and flag[i][j] == False:
            q.append((i, j))
            flag[i][j] = True
            size = 1

            while q:  # queue is not empty
                loc_x, loc_y = q.popleft()

                for index in range(4):
                    x = loc_x + dx[index]
                    y = loc_y + dy[index]

                    if x < 0 or x >= n or y < 0 or y >= m:  # 범위 index를 넘어선다면
                        continue

                    if flag[x][y] == False and arr[x][y] == 1:  # 아직 다녀가지 않았는데, 그림의 영역이라면
                        q.append((x, y))
                        flag[x][y] = True
                        size += 1

            answer.append(size)

if len(answer) == 0:
    print(len(answer))
    print(0)
else:
    print(len(answer))
    print(max(answer))
