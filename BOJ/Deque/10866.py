import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dq = deque()
for i in range(N):
    order = input().split()

    if order[0] == "push_back":
        dq.append(order[1])

    elif order[0] == "push_front":
        dq.appendleft(order[1])

    elif order[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif order[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)

    elif order[0] == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)

    elif order[0] == "pop_back":
        if dq:
            print(dq.pop())

        else:
            print(-1)

    elif order[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)

    elif order[0] == "size":
        print(len(dq))
