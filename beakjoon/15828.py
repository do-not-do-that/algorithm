# 버퍼에는 라우터에 입력으로 들어온 패킷들이 순서대로 위치하고,
# 라우터에서는 먼저 온 패킷부터 하나씩 처리 후 버퍼에서 제거
# 버퍼에 다 차있으면, 이후 들어오는 데이터는 다 버려짐
# 양의 정수 : 해당 번호의 패킷 들어옴
# 0 : 라우터는 패킷 하나 처리함.
# -1: 입력 끝

# 50점..???
# buffer_size = int(input())  # 버퍼 크기
# buffer = []

# while True:
#     N = int(input())

#     if N == -1:
#         break
#     elif N == 0:
#         buffer.pop(0)
#     else:
#         if len(buffer) < buffer_size:
#             buffer.append(N)


# print(*buffer if len(buffer) else "empty")


# deque 사용하면 맞출 수 있을 것 같다.
import sys
from collections import deque

input = sys.stdin.readline

buffer_size = int(input())  # 버퍼 크기
buffer = deque()

while True:
    N = int(input())

    if N == -1:
        break
    if N == 0:
        buffer.popleft()
    if N and len(buffer) < buffer_size:
        buffer.append(N)


print(*buffer if len(buffer) else "empty")

# 배운 점 : 입력되는 라인 수가 많아 백준에서 부분 정답을 맞는 경우, sys import 해서
# input 을 대체하자!
