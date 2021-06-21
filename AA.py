import sys
sys.stdin = open('./input.txt','rt')

n = int(input())    
a = list(input().split())

def reverse(x):
    return int(x[::-1])

def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x//2+1):
        if x % i == 0:
            return False
    
    return True

for idx, x in enumerate(a):
    a[idx] = reverse(x)
    if isPrime(a[idx]) == True:
        print(a[idx],end=' ')

    
