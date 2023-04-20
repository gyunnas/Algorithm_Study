import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    num = int(input())
    dp = [0] * (num + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for n in range(4, num + 1):
        dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]

    print(dp[num])
