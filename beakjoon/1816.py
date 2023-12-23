# S 가 주어지면, S의 모든 소인수가 10^6 보다 큰가?
# 시간 초과 -> 해결!


def is_validate(s):
    # 짝수 거름
    if s % 2 == 0:
        return False

    # n이 10^6 보다 작다면 거름
    for i in range(3, 10**6):
        if s % i == 0:
            return False

    return True


N = int(input())

for _ in range(N):
    s = int(input())
    if is_validate(s):
        print("YES")
    else:
        print("NO")
