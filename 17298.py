import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int, input().split()))

stack=[0]
answer=[-1]*n

for i in range(1,n):
    while stack and data[stack[-1]] < data[i]:
        answer[stack.pop()] = data[i]
    stack.append(i)

print(*answer)