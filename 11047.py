n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
cnt = 0

for i in data[::-1]:
    if k == 0:
        break
    if (tmp:=k//i)>0:
        cnt += tmp
        k %= i

print(cnt)