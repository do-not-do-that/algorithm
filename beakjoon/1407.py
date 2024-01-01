import sys

input = sys.stdin.readline

# 시간 초과 나는 코드.
# A, B = map(int, input().split())
# answer = 0
# tmp = 1

# for i in range(A, B + 1):
#     if i % 2 != 0:
#         answer += 1
#         continue

#     n = i
#     tmp = 1

#     while n % 2 == 0:
#         tmp *= 2
#         n //= 2
#     answer += tmp


# print(answer)


# 최적화 작업
A, B = map(int, input().split())
A -= 1
tmp_A = A
tmp_B = B

for i in range(1, 99):
    tmp_A += (A // 2**i) * (2**i - 2 ** (i - 1))
    tmp_B += (B // 2**i) * (2**i - 2 ** (i - 1))


print(tmp_B - tmp_A)
