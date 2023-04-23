import sys

input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(dp[1] + stairs[2], dp[0] + stairs[2])

for k in range(3, N):
    dp[k] = max(dp[k - 3] + stairs[k - 1] + stairs[k], dp[k - 2] + stairs[k])

print(dp[N - 1])
