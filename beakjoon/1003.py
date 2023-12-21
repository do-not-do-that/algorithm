###### 첫번째 접근 ######
# 그냥 실제로 함수 만들어서 돌려보면 ? -> 시간초과
# def func(n):
#     zero_cnt = 0
#     one_cnt = 0

#     def fibonacci(n):
#         nonlocal zero_cnt, one_cnt
#         if n == 0:
#             zero_cnt += 1
#             return 0
#         elif n == 1:
#             one_cnt += 1
#             return 1
#         else:
#             return fibonacci(n - 1) + fibonacci(n - 2)

#     fibonacci(n)
#     print(zero_cnt, one_cnt)


# T = int(input())
# n_list = [int(input()) for _ in range(T)]
# for n in n_list:
#     func(n)


##### 두번째 접근 #####
# 각 항마다 0과 1이 몇 번 나오는지 미리 계산해서 저장
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)


# 피보나치 수열에서 특정 항의 0과 1 등장횟수 == 이전 두 항의 해당 숫자의 등장 횟수의 합
# n 번째 항에서의 0과 1의 등장 횟수 == n-1 에서의 0과 1 등장 횟수 + n-2 에서의 0과 1 등장 횟수
# 3 번째 항에서 0과 1의 등장 횟수 == F(2)와 F(1) 에서의 등장 횟수
def count_fibonacci_numbers(max_n):
    zero_count = [1, 0] + [0] * (max_n - 1)
    one_count = [0, 1] + [0] * (max_n - 1)

    for i in range(2, max_n + 1):
        zero_count[i] = zero_count[i - 1] + zero_count[i - 2]
        one_count[i] = one_count[i - 1] + one_count[i - 2]

    return zero_count, one_count


T = int(input())
n_list = [int(input()) for _ in range(T)]
max_n = max(n_list)
zero_count, one_count = count_fibonacci_numbers(max_n)

for n in n_list:
    print(zero_count[n], one_count[n])
