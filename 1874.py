import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())

stack = [1]
data = deque([int(input().rstrip()) for _ in range(n)])
s = ['+']
pointer = 1
while data:
    if stack and stack[-1] < data[0]:
        pointer+=1
        stack.append(pointer)
        s.append('+')
    elif stack and stack[-1] == data[0]:
        stack.pop()
        data.popleft()
        s.append('-')
    elif not stack:
        pointer+=1
        stack.append(pointer)
        s.append('+')
    else:
        print('NO')
        sys.exit(0)

print('\n'.join(map(str, s)))





















