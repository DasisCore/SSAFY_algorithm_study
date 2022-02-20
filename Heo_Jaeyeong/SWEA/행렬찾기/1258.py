# 1258. 행렬찾기

import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    n = int(input())
    li = [list(map(int, input().split())) for i in range(n)]

    dic= {}
    for i in li: # 각 행과 열을 딕셔너리 형태로 만듬.
        s = 0
        cnt = 0
        while s < len(i):
            if i[s] == 0:
                if not cnt in dic: # 딕셔너리에 값이 없으면 새로 생성
                    dic[cnt] = 1
                else: # 딕셔너리에 값이 있으면 +1
                    dic[cnt] += 1
                cnt = 0
                s += 1 # 한칸 전진

            elif i[s] != 0:
                cnt += 1
                s += 1
        else:
            if not cnt in dic: # 0이 안나오고 행이 끝나면 카운트가 되지 않으므로
                dic[cnt] = 1
            else:
                dic[cnt] += 1

    matrix = []
    for o, k in dic.items():
        if o != 0:
            matrix.append([k, o, k * o])

    matrix.sort(key = lambda x : (x[2], x[0]))
    # 2차원 리스트의 2번 리스트를 기준으로 정렬, 같을 경우 두번 째 인자를 기준으로 다시 정렬

    print(f"#{_ + 1} {len(matrix)}", end = " ") # 출력 형식 지키기
    for i in matrix:
        print(*i[0:2], end = " ")
    print()
