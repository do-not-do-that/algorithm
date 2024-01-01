import sys

input = sys.stdin.readline

# 아주 옛날 옛 적에 풀었던 코드...
# 메모리는 30860KB, 시간은 68ms 이었다.
# def is_prime_number(target):
#     if target  < 2:
#         return False
#     for i in range(2, target):
#         if target % i == 0:
#             return False

#     return True

# N = int(input())

# data = list(map(int, input().split()))
# res= []

# for target in data:
#     res.append(is_prime_number(target))

# print(len([i for i in res if i == True]))


# 최적화해보자.
# 시간이 40ms 로 줄었다.
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


N = int(input())
nums = list(map(int, input().split()))
print(len([1 for n in nums if is_prime(n)]))
