# for 루프가 break 를 만나지 않으면 else 실행

import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
beer_list = [list(map(int, input().split())) for _ in range(K)]

# 도수 순으로 정렬
beer_list.sort(key=lambda x: x[1])

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
            prefer -= heapq.heappop(q)  # 가장 작은 만족도를 가지고 있는 맥주 뺌(선호도에서 제거)
else:
    print(-1)
    exit()


print(answer)
