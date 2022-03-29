n = int(input())
p = list(map(int, input().split()))
p.sort()
total = 0
for idx, value in enumerate(p):
    total+=(n-idx)*value
print(total)