# from collections import deque
# import sys
# input = sys.stdin.readline
# n = int(input().rstrip())

# stack = deque([])
# data = deque([int(input().rstrip()) for _ in range(n)])
# arr = [i for i in range(n, 0, -1)]
# s = []

# while data:
#     if stack and stack[-1] == data[0]:
#         stack.pop()
#         s.append('-')
#         data.popleft()
#         continue
#     if not arr:
#         data.reverse()
#         if data != stack:
#             print('NO')
#             s.clear()
#             break
#     if arr[-1] < data[0]:
#         stack.append(arr.pop())
#         s.append('+')
#     elif arr[-1] == data[0]:
#         stack.append(arr.pop())
#         s.append('+')
#         stack.pop()
#         s.append('-')
#         data.popleft()
    
# if s:
#     print('\n'.join(map(str, s)))

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





















