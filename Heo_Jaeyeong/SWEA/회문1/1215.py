# 1215. 회문1

import sys
sys.stdin = open("input.txt")


for _ in range(10):
    n = int(input())
    li = [list(input()) for i in range(8)]

    def check(li, n): # 2차원 리스트에서 글자 수가 4개인 회문을 찾는 함수
        answer = 0
        for i in li: # 총 8줄을 돌아야 하므로
            for j in range(8 - n + 1): # 한 줄에서 나올 수 있는 4개짜리 회문
                temp = []
                for k in range(n): # 회문인지 확인해야 할 문장
                    temp.append(i[j + k])
                if temp == temp[::-1]: # 회문이면 answer +1
                    answer += 1
        else:
            return answer

    total = 0
    total += check(li, n)

    # 전치행렬 만들기
    for i in range(8): # 이유 : 전치행렬을 쓰면 행만 확인하면 되므로
        for j in range(8):
            if i > j:
                li[i][j], li[j][i] = li[j][i], li[i][j]

    total += check(li, n)
    print(f"#{_ + 1} {total}")



