candy = int(input())
cnt = 0
for A in range(1, candy + 1):
    for B in range(1, candy + 1):
        for C in range(1, candy + 1):
            if A + B + C == candy:
                if A >= 2 + B:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            cnt += 1

print(cnt)
