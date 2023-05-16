import sys


# num: 현재 몇 개의 숫자를 사용했는가?
def get_nm(num):
    if num == M + 1:
        print(" ".join(map(str, arr)))

    for i in range(1, N + 1):  # 1부터 N번째 수까지
        if not is_used[i]:
            arr.append(i)
            is_used[i] = True
            get_nm(num + 1)
            is_used[i] = False
            arr.pop()


input = sys.stdin.readline

# 1부터 N까지 중복 없이 M개를 고른 수열
N, M = map(int, input().split())

# 해당 숫자를 사용 했는가? 0 부터 N번 인덱스
is_used = [False] * (N + 1)

# 해당 숫자가 담긴 리스트 0 부터 M번 인덱스
arr = []

get_nm(1)
