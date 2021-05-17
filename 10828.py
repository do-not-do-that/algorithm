import sys
sys.stdin = open('case.txt')
def push():
    answer.append(command[i][1])
def pop():
    if len(answer)==0:
        return print(-1)
    print(answer.pop())
def size():
    print(len(answer))
def empty():
    if answer:
        return print(0)    
    print(1)
def top():
    if len(answer)==0:
        return print(-1)
    print(answer[-1])
n = int(input())
command=[]
answer=[]
for i in range(n):
    command.append(list(sys.stdin.readline().split()))
    if command[i][0]=="push":
        push()
    elif command[i][0]=="pop":
        pop()
    elif command[i][0]=="size":
        size()
    elif command[i][0]=="empty":
        empty()
    elif command[i][0]=="top":
        top()

