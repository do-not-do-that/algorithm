import sys
input = sys.stdin.readline

def DFS(L, s):
    if L == m:
        print(" ".join(map(str, res)))
        return
    
    for i in range(s, n+1):
        res.append(i)
        DFS(L+1, i+1)
        res.pop()




n, m =map(int, input().split())
res=[]
DFS(0, 1)