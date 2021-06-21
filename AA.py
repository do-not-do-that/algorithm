import sys
# sys.stdin = open('./input.txt','rt')

n = int(input())
a = list(map(int,input().split()))
sum=0
tmp=0
for i in a:
    if i==1:
        tmp+=1
        sum+=tmp
    else:
        tmp=0
print(sum)
