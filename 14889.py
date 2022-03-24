from itertools import combinations as c
import sys
n = int(input())
arr = list(c([i for i in range(n)], int(n//2))) # 경우의 수가 담겨있는 조합 데이터
data = [list(map(int, input().split())) for _ in range(n)]
minimun = 2147000000


for a in arr:
    team_a = 0
    team_b = 0
    for i in a:
        for j in a:
            team_a+=data[i][j]
    b = [m for m in range(n) if m not in a]
    for i in b:
        for j in b:
            team_b+=data[i][j]
    minimun = min(minimun, abs(team_a-team_b))

print(minimun)

