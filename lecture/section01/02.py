# K번째 수
# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열 중에서 s번째부터 e번째 까지의 수를
# 오름차순 정렬했을 때 k 번째로 나타나는 숫자를 출력하라

T = int(input())
for t in range(T):
    N, s, e, k = map(int, input().split())
    data = list(map(int, input().split()))
    tmp = sorted(data[s - 1 : e])
    print("#{t} {v}".format(t=t + 1, v=tmp[k - 1]))
