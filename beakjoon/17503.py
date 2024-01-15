import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())


beer_list = [list(map(int, input().split())) for _ in range(K)]
beer_list = sorted(beer_list, key=lambda x: (x[1], x[0]))

prefer = 0
q = []

# 낮은 도수부터 먹어보면서 N을 만족하는지 확인
# 만족하지 않으면 -1 출력하고 종료
for i in beer_list:
    prefer += i[0]
    heapq.heappush(q, i[0])

    if len(q) == N:  # 오늘이 마지막 날이면
        if prefer >= M:  # 선호도 충족
            answer = i[1]  # 현재 도수레벨
            break
        else:
            prefer -= heapq.heappop(q)
else:
    print(-1)
    exit()


print(answer)
