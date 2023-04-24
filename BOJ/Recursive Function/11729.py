import sys

input = sys.stdin.readline


def hanoi(start, by, end, num):
    if num == 1:
        print(start, end)
    else:
        hanoi(start, end, by, num - 1)
        print(start, end)
        hanoi(by, start, end, num - 1)


n = int(input())
print((2**n) - 1)
hanoi(1, 2, 3, n)
