import sys
input = sys.stdin.readline


def dfs(L, total, plus, minus, multi, devide):
    global maximum, minimum
    if L == n:
        minimum = min(total, minimum)
        maximum = max(total, maximum)
        return
    
    if plus:
        dfs(L+1, total+data[L], plus-1, minus, multi, devide)
    if minus:
        dfs(L+1, total-data[L], plus, minus-1, multi, devide)
    if multi:
        dfs(L+1, total*data[L], plus, minus, multi-1, devide)
    if devide:
        dfs(L+1, int(total/data[L]), plus, minus, multi, devide-1)

maximum = -1247000000
minimum = 1247000000

n = int(input())
data = list(map(int, input().split()))
oper = list(map(int, input().split()))
dfs(1, data[0], oper[0], oper[1], oper[2], oper[3])

print(maximum)
print(minimum)
