# 직접 나눗셈 하지 않고, 문자열로 풀어보장
N = int(input())
hints = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for a in range(1, 10):  # 100의 자릿수
    for b in range(1, 10):  # 10의 자릿수
        for c in range(1, 10):  # 1의 자릿수
            if a == b or b == c or c == a:
                continue
            cnt = 0
            for hint in hints:
                strike_cnt = 0
                ball_cnt = 0
                num, strike, ball = hint

                s_num = str(num)
                A = str(a)
                B = str(b)
                C = str(c)
                # strike
                if s_num[0] == A:
                    strike_cnt += 1
                if s_num[1] == B:
                    strike_cnt += 1
                if s_num[2] == C:
                    strike_cnt += 1

                # ball
                if s_num[0] != A and A in s_num:
                    ball_cnt += 1
                if s_num[1] != B and B in s_num:
                    ball_cnt += 1
                if s_num[2] != C and C in s_num:
                    ball_cnt += 1

                if strike == strike_cnt and ball == ball_cnt:
                    cnt += 1

            if cnt == N:
                ans += 1

print(ans)
