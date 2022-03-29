import sys
input = sys.stdin.readline
n = int(input().strip())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x:x[0])
out = []
cnt = 0

while data:
    endpoint = 0
    for i in range((l:=len(data))):
        if data[i][0] >= endpoint:
            endpoint = data[i][1]
            out.append(i)

    for i in out:
        if i == l-1:
            data.pop()
        else:
            data.pop(i)
    print(data)
    out.clear()
    cnt+=1


print(cnt)


