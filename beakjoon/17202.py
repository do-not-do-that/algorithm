# 핸드폰 번호 궁합
import sys

input = sys.stdin.readline

a = list(input())
b = list(input())

ans = ""
tmp = []

for i in range(8):
    ans += a[i] + b[i]


while len(ans) > 2:
    for i in range(len(ans) - 1):
        tmp.append(str(((int(ans[i]) + int(ans[i + 1])) % 10)))
    ans = "".join(tmp)
    tmp = []


print(ans)
