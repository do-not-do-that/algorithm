import sys

input = sys.stdin.readline


def is_prime(N):
    if N == 1:
        return False
    else:
        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                return False
    return True


def is_palindrome(N):
    if str(N) == str(N)[::-1]:
        return True
    return False


N = int(input())
result = 0

while True:
    if is_prime(N) and is_palindrome(N):
        result = N
        break
    N += 1

print(result)


# 틀렸던 코드, N의 범위가 정답의 범위는 아님

# for i in range(N, 1000001):
#     if is_prime(i) and is_palindrome(i):
#         result = i
#         break

# print(result)
