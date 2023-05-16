import sys

input = sys.stdin.readline


def dfs(start):
    global cnt

    if li and sum(li) == S:
        cnt += 1

    if start == N + 1:
        return

    for i in range(start, len(arr)):
        li.append(arr[i])  # 부분 수열에 포함 시키거나
        dfs(i + 1)
        li.pop()  # 부분 수열에 포함시키지 않음


N, S = map(int, input().split())
arr = list(map(int, input().split()))
li = []
cnt = 0

dfs(0)

print(cnt)
