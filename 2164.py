import sys
from collections import deque
sys.stdin = open('case.txt')
n = int(input())
arr = deque(i+1 for i in range(n))

for i in range(n-1):
    arr.popleft()
    arr.append(arr.popleft())
    
print(arr[0])
