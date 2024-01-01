import sys

input = sys.stdin.readline


# 아래는 시간 초과나는 코드
# def SOD(n):
#     sum_res = 0
#     for i in range(2, n):
#         if n % i == 0:
#             sum_res += i
#     return sum_res


# def CSOD(n):
#     ans = 0
#     for i in range(1, n + 1):
#         ans += SOD(i)
#     return ans % 1000000

# n = int(input())

# print(CSOD(n))
# TODO : 이 문제 다시 풀어보기.
import sys

input = sys.stdin.readline
n = int(input())
answer = 0

for i in range(2, int(n**0.5) + 1):
    j = n // i
    answer += (j + i) * (j - i + 1) // 2
    answer += (j - i) * i
print(answer % 1000000)
