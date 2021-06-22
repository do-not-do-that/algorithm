import sys
sys.stdin =open('./input.txt','rt')

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

s=e=n//2
res=0
for i in range(n):
    for j in range(s,e+1):
            res+=a[i][j]
    if i < n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)
        
    


# 내 풀이

# mt = n//2
# pointer = 0
# tot = 0

# for i in range(n):
#     if i <= mt:
#         for j in range(mt-i,mt+i+1):
#             tot+=a[i][j]
#     else:
#         for j in range(mt-(n-i-1),mt+(n-i)):
#             tot+=a[i][j]

# print(tot)




