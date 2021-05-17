import sys
sys.stdin = open('case.txt')
n = int(input())

for _ in range(n):
    check=list(input())
    ans=0
    for i in check:
        if i=="(":
            ans+=1
        else :
            ans-=1
        if ans<0:
            print('NO')
            break
    else:
        if ans==0:
            print('YES')
        else:
            print('NO')
        
    


print(check)

