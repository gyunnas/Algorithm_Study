import sys

input = sys.stdin.readline


def POW(A, B, C):  # A를 B번 곱한 것을 C로 나눈 나머지
    if B == 1:
        return A % C

    if B % 2 == 0:
        return (POW(A, B // 2, C) ** 2) % C

    else:
        return ((POW(A, (B // 2), C) ** 2) * A) % C


A, B, C = map(int, input().split())
print(POW(A, B, C))
