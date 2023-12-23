# 서로 다른 숫자
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
                num, strike, ball = hint

                num_list = []
                num_list.append(num // 100)  # num 의 첫번째 자리수
                num_list.append((num % 100) // 10)  # num 의 두번째 자리수
                num_list.append((num % 100) % 10)  # num 의 세번째 자리수

                strike_cnt = 0
                ball_cnt = 0

                # strike 개수 구하기
                if num_list[0] == a:
                    strike_cnt += 1
                if num_list[1] == b:
                    strike_cnt += 1
                if num_list[2] == c:
                    strike_cnt += 1

                # ball 개수 구하기
                if num_list[0] != a and a in num_list:
                    ball_cnt += 1
                if num_list[1] != b and b in num_list:
                    ball_cnt += 1
                if num_list[2] != c and c in num_list:
                    ball_cnt += 1

                if strike == strike_cnt and ball == ball_cnt:
                    cnt += 1

            if cnt == N:
                ans += 1

print(ans)
