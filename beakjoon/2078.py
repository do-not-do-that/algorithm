# 역으로 루트까지 올라가기..?
####### 첫번째 시도 #######
# 시간 초과.
# def find_node(L, R):
#     left_moves = 0
#     right_moves = 0
#     while L != 1 or R != 1:
#         if L > R:
#             left_moves += 1
#             L -= R
#         else:
#             right_moves += 1
#             R -= L
#     return left_moves, right_moves


# L, R = map(int, input().split())
# print(*find_node(L, R))


####### 두번째 시도 #######
# 한쪽으로 치우쳐진 케이스 때문에 실패하는 것 같음. 올라가는 단위..를 크게?


def find_node(L, R):
    left_moves = 0
    right_moves = 0
    while L != 1 or R != 1:
        if L > R:
            moves = (L - 1) // R
            left_moves += moves
            L -= R * moves
        else:
            moves = (R - 1) // L
            right_moves += moves
            R -= L * moves
    return left_moves, right_moves


L, R = map(int, input().split())
print(*find_node(L, R))
