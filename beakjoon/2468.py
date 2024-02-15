import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# 물에 잠기지 않는 안전한 영역이란
# 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며
# 그 크기가 최대인 영역


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 이동을 위한 배열
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0


# x,y 에서 시작하여 높이 h 이상인 인접 지점 탐색
def dfs(x, y, h):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > h and not visited[nx][ny]:
            dfs(nx, ny, h)


for h in range(101):  # 0부터 높이의 max인 101까지
    tmp = 0
    visited = [[False for _ in range(N)] for _ in range(N)]  # 방문 여부
    for i in range(N):
        for j in range(N):
            if board[i][j] > h and not visited[i][j]:  # 현재 위치에서 안전영역을 찾아 추가
                dfs(i, j, h)
                tmp += 1
    cnt = max(cnt, tmp)

print(cnt)
