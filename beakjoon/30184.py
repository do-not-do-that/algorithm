def min_operations_to_form_grades_optimized(N, grades):
    operations = []
    cursor_position = 0  # 커서의 초기 위치

    # 'S'와 'U'의 개수를 세어 필요한 연산 횟수를 결정
    count_S = grades.count("S")
    count_U = grades.count("U")

    while count_S > 0 and count_U > 0:
        if grades[cursor_position] == "S":
            # 'S'를 추가하기 위해 'SU'를 추가
            operations.append("S")
            cursor_position += 2
            count_S -= 1
        else:
            # 'U'를 추가하기 위해 'US'를 추가하고 커서를 왼쪽으로 옮김
            operations.append("U")
            operations.append("N")  # 커서를 왼쪽으로 옮김
            cursor_position += 1
            count_U -= 1

    # 시행 횟수와 시행의 연속을 반환
    return len(operations), "".join(operations)


# 결과 계산
result = min_operations_to_form_grades_optimized(int(input()), input())
print(result)
