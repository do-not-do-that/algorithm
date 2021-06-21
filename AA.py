import sys
# sys.stdin = open('./input.txt','rt')

n = int(input())
students = list(map(int,input().split()))
avg = round(sum(students)/n)
min = float('inf')
for idx, x in enumerate(students):
    tmp = abs(x-avg)
    if tmp<min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x>score:
            score = x
            res = idx+1
print('%d %d' %(avg, res))
