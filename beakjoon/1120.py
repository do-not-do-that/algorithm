# A 와 B 가 같아질 때까지 아래 연산
# A 앞에 아무 알파벳이나 추가
# A 뒤에 아무 알파벳이나 추가
# A 와 B의 길이가 같으면서, A 와 B의 차이를 최소로 하는 프로그램

# A 문자열 앞뒤에 B와 같은 알파벳을 넣으면 됨.
# B 를 기준점으로 두고, 이를 A 와 비교하여 차이가 최소가 되면 그 수를 출력하는 문제.

# 첫번째 for 문은 A 가 B 내에서 취할 수 있는 모든 시작 위치의 수.


A, B = input().split()
min_val = len(A)  # 최대값은 A의 문자열 길이

for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):  # A 의 길이에서 추가되는 만큼은 어차피 B 랑 동일한 문자가 들어가기 때문에, A만큼만 비교
        if A[j] != B[i + j]:  # 현 상태에서 다른 문자 개수 체크
            cnt += 1
    min_val = min(min_val, cnt)

print(min_val)
