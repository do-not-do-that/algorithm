import sys
sys.stdin =open('./input.txt','rt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
a = [[0]*(n+2)]+[[0]+list(map(int,input().split()))+[0] for _ in range(n)]+[[0]*(n+2)]
cnt=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)


# 내 풀이
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and a[i][j] > a[i][j+1] and a[i][j] > a[i][j-1]:
#             cnt+=1

# print(cnt)





