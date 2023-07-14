# k번째 약수
# 자연수 N과 K가 주어졌을 때 N의 약수들 중 K번째로 작은 수를 출력하라

n, k = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
