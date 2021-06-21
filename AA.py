import sys
# sys.stdin = open('./input.txt','rt')

a = [str(i) for i in range(1,21)]


for _ in range(10):
    ai,bi = map(int,input().split())
    tmp = a[ai-1:bi]
    tmp=tmp[::-1]
    a[ai-1:bi] = tmp
print(' '.join(a))