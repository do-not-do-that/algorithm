import sys
sys.stdin = open('./input.txt','rt')

n = int(input())
a=[]
for i in range(n):
    s = input()
    s = s.lower()
    if s == s[::-1]:
        print('#%d YES' %(i+1))
    else:
        print('#%d NO' %(i+1))


