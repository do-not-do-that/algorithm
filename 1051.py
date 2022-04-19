
n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        for k in range(min(n, m)):
            if (i + k < n) and (j + k < m) and (data[i][j] == data[i][j + k] == data[i + k][j] == data[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
                
print(answer)