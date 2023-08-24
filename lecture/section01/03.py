#  1부터 100사이의 자연수가 적힌 N장의 카드가 있다.
# 같은 숫자의 카드가 여러 장 있을 수 있고, 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록한다.
# 3장을 뽑을 수 있는 모든 경우의 수를 기록하고, 기록한 값 중 K번째로 큰 수를 출력한다.
# K번째 수는 반드시 존재한다.

import sys

sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
cards = list(map(int, input().split()))
