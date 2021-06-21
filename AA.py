import sys
# sys.stdin = open('./input.txt','rt')

t = int(input())

for i in range(t):
    n,s,e,k = map(int,input().split())
    li = list(map(int,input().split()))
    tmp = li[s-1:e]
    tmp.sort()
    print('#%d %d'%(i+1,tmp[k-1]))

