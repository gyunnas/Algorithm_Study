import sys

input = sys.stdin.readline


def square(N, r, c):
    if N == 0:
        return 0

    half = 2 ** (N - 1)
    # 첫 번째 사각형
    if r < half and c < half:
        return square(N - 1, r, c)

    # 두 번째 사각형
    elif r < half and c >= half:
        return half * half + square(N - 1, r, c - half)

    # 세 번째 사각형
    elif r >= half and c < half:
        return 2 * half * half + square(N - 1, r - half, c)

    else:
        return 3 * half * half + square(N - 1, r - half, c - half)


N, r, c = map(int, input().split())
print(square(N, r, c))
