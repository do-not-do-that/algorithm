# 가장 유명한 사람을 구하는 방법 : 2-친구를 구하면 됨.
# 2-친구란, 두 사람이 친구이거나 A와 친구고, B와 친구인 C가 존재해야한다.

import sys
import copy

input = sys.stdin.readline


N = int(input())  # 50보다 작거나 같은 자연수
d = {}
result = {}

# {0: [1, 2]}

# 1. 자기 친구만 추가
# 자신의 친구만 추가
for i in range(N):
    str = input()
    depth = 0
    d[i] = [idx for idx, c in enumerate(str) if c == "Y"]

# deep copy
result = copy.deepcopy(d)

# 친구의 친구도 추가
for key, val in d.items():
    for i in val:
        # 자기 자신 빼기
        result[key] = result[key] + [c for c in d[i] if key != c]

print(max([len(set(arr)) for arr in result.values()]))
