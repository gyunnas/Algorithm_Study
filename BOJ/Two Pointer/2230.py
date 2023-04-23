import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

i, j = 0, 0
A = sorted(A)
value = sys.maxsize

for j in range(N):
    while i <= j and A[j] - A[i] >= M:
        value = min(value, A[j] - A[i])
        i += 1

print(value)
