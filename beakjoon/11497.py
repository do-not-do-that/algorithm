# 높이 차가 최소 -> 정렬문제.
# 서로 간의 간격이 최소차가 되도록 정렬하면 됨.

# 높이차 최소 아이디어 : 가장 큰 걸 중심으로 양 옆에 그 다음으로 큰걸 두면 됨.
# 2, 4, 5, 7, 9 -> 9를 중심으로 앞 2번째인덱스 뒤로 보낸다고 생각하면 됨

import sys

input = sys.stdin.readline


def leveling(N, L):
    L.sort()
    level = 0
    for i in range(2, N):
        level = max(level, abs(L[i] - L[i - 2]))
    print(level)


T = int(input())

for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    leveling(N, L)
