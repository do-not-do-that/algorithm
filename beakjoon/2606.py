import sys

input = sys.stdin.readline


# 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어있는 정보가 주어질 때,
# 1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 수를 출력

# 1058 문제랑 거의 흡사한 것 같음. 근데 단계가 좀 더 깊어진?


N = int(input())
pair = int(input())
results = []
network = {}
log = [1]


def make_z(layer):
    global results
    results = results + layer

    for l in layer:
        if l not in log:
            log.append(l)
            make_z(network[l])


# network 구성도 생성하기
for _ in range(pair):
    a, b = map(int, input().split())

    if not network.get(a):  # 등록되지 않은 컴퓨터일 경우
        network[a] = [b]
    else:
        network[a].append(b)

    if not network.get(b):
        network[b] = [a]
    else:
        network[b].append(a)

    if a == 1:
        results.append(b)

# 완성된 네트워크
# {1: [2, 5], 2: [1, 3, 5], 3: [2], 5: [1, 2, 6], 6: [5], 4: [7], 7: [4]}
# 1과 연결된 컴퓨터가 하나도 없을 경우?

if network.get(1):
    layer = network[1]
    make_z(layer)

print(len(log) - 1)
