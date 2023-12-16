# 라운드가 끝날 때, 가장 작은 인덱스에 승원의 rank 가 있으면 됨.
# 라운드가 2N 을 넘어가면, 반복이기 때문에 라운드 도는 for 의 반복은 R을 2N 으로 나눈 나머지만 돌면 됨.


def play(N, R, my_rank, others_rank, start_pos):
    # 토너먼트 시작 후 승원이와 다른 궁수들의 초기위치 설정
    current_pos = others_rank[:]
    current_pos.insert(start_pos - 1, my_rank)

    for r in range(R):  # 라운드 수행
        print("=========", r + 1, "라운드=========")

        for i in range(1, N):
            # 각 표적에서 승패 결정할 수 있음
            left_index = 2 * i
            right_index = 2 * i + 1

            # 위치 교환을 어떻게 해야할지 잘 모르겠음.
            if current_pos[left_index] > current_pos[right_index]:
                # 낮은 랭크를 가진 궁수(오른쪽 궁수)가 이긴 경우, 위치 교환
                current_pos[left_index], current_pos[right_index] = (
                    current_pos[right_index],
                    current_pos[left_index],
                )
            else:
                pass

        # 1번 표적의 패자는 N번 표적으로 이동
        current_pos.append(current_pos.pop(0))
    return current_pos.index(my_rank) + 1


def find_best_start_position(N, R, my_rank, others_ranks):
    best_pos = 1
    best_final_pos = 2 * N

    for start_pos in range(1, 2 * N + 1):
        final_pos = play(N, R, my_rank, others_ranks, start_pos)
        print("처음 위치 : ", start_pos, "마지막 포지션 : ", final_pos)
        if final_pos <= best_final_pos:
            best_final_pos = final_pos
            best_pos = start_pos

    return best_pos


N, R = map(int, input().split())
my_rank = int(input())
others_rank = [int(input()) for _ in range(2 * N - 1)]

best_start = find_best_start_position(N, R, my_rank, others_rank)

print("best : ", best_start)
