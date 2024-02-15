import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
count = [0 for _ in range(F)]  # 횟수 체크


def bfs():
    global flag
    q = deque()
    q.append(S)
    count[S] = 1  # 초기 위치
    while q:
        cur = q.popleft()  # 큐에서 층 하나씩 꺼냄
        if cur == G:  # 목적지 도착
            flag = True
            print(count[cur] - 1)
            break
        for i in (U, -D):  # 위, 아래로 이동
            next = cur + i  # 층 수
            if 1 <= next <= F and count[next] == 0:  # # F층과 같거나 아래에 있으면서 와본 적 없으면
                count[next] = count[cur] + 1  # next 층의 카운트는 현재 카운트 +1
                q.append(next)  # 현재 층 추가


flag = False
bfs()

if flag == False:  # 도착 불가능이면
    print("use the stairs")
