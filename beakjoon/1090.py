# 1번 - 완전탐색
# 모든 경우의 수 다 탐색하기.

# 2번 - 이미 체커가 있는 곳에서의 경우의 수만 탐색하기
# (한 곳에서 모일 때, 비용을 최소화 하기위해서는 체커가 있는 곳 중 한 곳으로 모이면 된다는 걸 바탕으로)

# 3번 - 2개의 체커가 모일때는, 그냥 가까운 2명의 거리만 더해주면 됨.


# 놓치고 있었던 것 :
# 1차원 좌표에서 의 최소비용은 우리의 집 중에서 하나 고르면 되는 것. 즉, N개 의 경우의 수
# 2차원 좌표에서의 최소비용은 x축의 경우의 수 * y축의 경우의 수 이므로 N*N 이 되는 것임.


N = int(input())
arr = []
arr_x = []
arr_y = []
ans = [float("inf")] * N


for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
    arr_x.append(x)
    arr_y.append(y)

for x in arr_x:
    for y in arr_y:
        # 거리 측정
        dist = []

        for ex, ey in arr:
            # 현재 선택된 장소까지 각 체커마다 움직여야하는 수 배열에 삽입
            dist.append((abs(x - ex) + abs(y - ey)))

        dist.sort()  # 가장 가까운 순으로 정렬

        d_sum = 0  # 모이는 체커당 움직이는 수
        for idx, val in enumerate(dist):
            d_sum += val
            ans[idx] = min(ans[idx], d_sum)

print(*ans)
