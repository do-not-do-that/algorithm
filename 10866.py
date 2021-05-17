import sys
from collections import deque
sys.stdin = open('case.txt')

ans=deque()
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0]=="push_front": ans.appendleft(command[1])
    elif command[0]=="push_back": ans.append(command[1])
    elif command[0]=="pop_front": print(ans.popleft() if ans else -1)
    elif command[0]=="pop_back": print(ans.pop() if ans else -1)
    elif command[0]=="size": print(len(ans))
    elif command[0]=="empty": print(0 if ans else 1)
    elif command[0]=="front": print(ans[0] if ans else -1)
    elif command[0]=="back": print(ans[-1] if ans else -1)
