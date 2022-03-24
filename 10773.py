
k = int(input())
data =[]

for i in range(k):
    n = int(input())
    if n == 0:
        data.pop()
    else:
        data.append(n)

print(sum(data))
