# 가로, 세로, 대각선 연결은 걸어갈 수 있는 사각형임.
# 1은 땅, 0은 바다
# 섬의 개수
# 갈 수 있는 곳까지 가서, 더 이상 갈 수 없을 때 +1
# 여길 들렀다 간다는걸 어떻게 알 수 있지 -> 갔다 온 곳은 못가게 객체 사용하는 걸로.
# for 문 3개 사용하면 될 것 같음.
# 아래 이동,

# dx = [-1, 0, 1]
# dy = [1, 0, -1]


dx = [
    -1,
]
dy = [1]


def trip(i, j, land, mmap):
    # 다녀간 곳 체크
    mmap[(i, j)] = 1

    #
    for _ in range(i, w):
        pass


while True:
    w, h = map(int, input().split())
    land = []
    mmap = {}
    # 입력 종료
    if w == 0 and h == 0:
        break

    # land 정보 생성
    for _ in range(w):
        land.append(list(map(int, input().split())))

    for i in range(w):
        for j in range(h):
            if (i, j) not in mmap:
                trip(i, j, land, mmap)
