import sys
# sys.stdin = open('./input.txt','rt')

n,m = map(int,input().split())

a = list(map(int,input().split()))

#포인터 두개로 가야할듯
cnt=0
tot=a[0]
lt=0
rt=1

while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(cnt)



