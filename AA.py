import sys
sys.stdin = open('./input.txt','rt')

def digit_sum(x):
    sum=0
    # while x>0:
    #     sum += x % 10
    #     x = x//10

    for i in str(x):
        sum+= int(i)
    
    return sum

n = int(input())
a = list(map(int,input().split()))
max=-2147000000
for i in a:
    tot = digit_sum(i)
    if tot>max:
        max=tot
        res = i

print(res)
