# 풀었던 문제.
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: (x[1], x[0]))

endpoint = 0  # 끝나는 시간
cnt = 0

for start, end in data:
    if start >= endpoint:
        endpoint = end
        cnt += 1


print(cnt)
