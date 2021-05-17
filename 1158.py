n, k = map(int,input().split())
arr = [i+1 for i in range(n)]

answer = []
num=0


for t in range(n):
  num += k-1
  if num >=len(arr):
    num = num%len(arr)

  answer.append(str(arr.pop(num)))

print("<",", ".join(answer)[:],">", sep='')