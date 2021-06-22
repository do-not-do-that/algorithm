import sys
# sys.stdin =open('./input.txt','rt')

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
cmd = [list(map(int,input().split())) for _ in range(m)]
s = 0
e = n
tot =0
for i in range(m):
    #왼쪽이라면
    if cmd[i][1]==0:
        for j in range(cmd[i][2]):
            tmp1 = a[cmd[i][0]-1]
            a[cmd[i][0]-1].append(tmp1.pop(0))
    else:
        for j in range(cmd[i][2]):
            tmp1 = a[cmd[i][0]-1]
            a[cmd[i][0]-1].insert(0,tmp1.pop())

for i in range(n):
    for j in range(s,e):
        tot += a[i][j]
    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(tot)





