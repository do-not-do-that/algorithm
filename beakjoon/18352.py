import sys

input = sys.stdin.readline


N, M, K, X = map(int, input().split())
load = {key: [] for key in range(1, N + 1)}

# 길 생성하기
for _ in range(M):
    A, B = map(int, input().split())
    if B not in load[A]:
        load[A].append(B)
    if A not in load[B]:
        load[B].append(A)

# BFS

# K 는 최단거리.
while True:
    for i in load[X - 1]:
        pass
print(load)
