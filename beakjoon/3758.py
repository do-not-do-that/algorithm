# 고려 사항
# 최종 점수
# 풀이 횟수
# 최근 점수

for _ in range(int(input())):
    # 팀의 개수, 문제 개수, 팀 id, 로그 개수
    n, k, t, m = map(int, input().split())
    board = [[0] * k for _ in range(n)]  # 팀 별 문제 점수
    count = [0] * n  # 제출 횟수
    time = [0] * n  # 제출 시간

    for ts in range(m):
        tid, pid, score = map(int, input().split())
        board[tid - 1][pid - 1] = max(board[tid - 1][pid - 1], score)  # 둘 중 최대값 들어감
        count[tid - 1] += 1  # 해당 팀의 문제 풀이 카운트 증가
        time[tid - 1] = ts  # 해당 팀의 제출 시간 증가

    result = []  # 점수 계산용 변수

    for idx, line in enumerate(board):  # 인덱스 값과 값 동시 변환
        result.append([idx, sum(line), count[idx], time[idx]])

    # 점수는 높을 수록 우선순위 높아짐
    # 제출 횟수는 낮을수록 우선순위 높아짐
    # 마지막 제출 시간은 낮을수록 우선순위 높아짐
    result.sort(key=lambda x: (-x[1], x[2], x[3]))

    for idx, line in enumerate(result):
        if line[0] == t - 1:  # for 문 돌면서 내 team id 찾음
            print(idx + 1)
