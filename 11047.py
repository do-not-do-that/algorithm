n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)
cnt = 0

for i in data:
    if k == 0:
        break
    if (tmp:=k//i)>0:
        cnt += tmp
        k = k%i

print(cnt)
    
