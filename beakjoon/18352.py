import sys
from collections import deque

input = sys.stdin.readline


# 도시 개수, 도로 개수, 거리 정보, 출발도시 번호
N, M, K, X = map(int, input().split())
load = {key: [] for key in range(1, N + 1)}

# 길 생성하기 (갈 수 있는 것만 체크해야함.)
for _ in range(M):
    A, B = map(int, input().split())
    load[A].append(B)

# load  =  {1: [2, 3], 2: [3, 4], 3: [], 4: []}


distance = [0] * (N + 1)  # 거리 정보 기록용
visited = [0] * (N + 1)  # 방문 체크용
queue = deque([X])

visited[X] = 1  # 시작위치 추가

while queue:
    now = queue.popleft()  # 현재 위치
    for j in load[now]:
        if visited[j] == 0:  # 방문하지 않은 도시라면(최단 거리이므로 해당 조건으로 제외시킴)
            queue.append(j)
            visited[j] = 1
            distance[j] = distance[now] + 1

# 조건에 맞는 도시 출력
result = [i for i in range(1, N + 1) if distance[i] == K]
print("\n".join(map(str, result)) if result else -1)
