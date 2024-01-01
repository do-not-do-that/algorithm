# 완전 탐색

# 첫번째 선수는 N개의 깃발 중 1의 배수에 해당하는 번호의 깃발 뒤집어 놓음
# 두번째 선수는 N개의 깃발 중 2의 배수에 해당하는 번호의 깃발을 뒤집어 놓음.
# i번째 선수는 i의 배수에 해당하는 번호의 깃발을 뒤집음.
# N번재 선수까지 진행한 후 상태의 깃발 중 백색이 위로 놓여있는 깃발 수 출력

# 해당 코드는 메모리 초과됨.

import sys

input = sys.stdin.readline

# N = int(input())

# flags = [0] * N

# for i in range(1, N + 1):
#     flags = [int(not f) if (idx + 1) % i == 0 else f for idx, f in enumerate(flags)]

# print(len([1 for f in flags if f]))


# 최적화 작업
# 규칙을 찾아보면... 신기하게 제곱수만 남는다!


# N = int(input())
# cnt = 0

# for i in range(1, N + 1):
#     if i**2 <= N:
#         cnt += 1
#     else:
#         break

# print(cnt)


# 조금 더 깨끗하게 풀어보자.
# 제곱수를 찾는 문제이니, 루트로 나눈 것을 정수화 시키면 답이 된다.

N = int(input())
print(int(N**0.5))
