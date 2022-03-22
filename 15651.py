import sys
input = sys.stdin.readline

def DFS(L):
    if L == m:
        print(" ".join(map(str, res)))
        return
    for i in range(1, n+1):
        res.append(i)
        DFS(L+1)
        res.pop()

n, m =map(int, input().split())
res = []
DFS(0)