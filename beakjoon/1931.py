# 풀었던 문제.
# 회의실을 최대로 사용하기 - 끝나는 시간이 짧은 것들만 선택 -> 그리디
import sys

input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0

for start, end in info:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)
