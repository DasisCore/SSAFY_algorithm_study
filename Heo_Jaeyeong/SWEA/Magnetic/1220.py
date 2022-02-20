# 1220. Magnetic

import sys
sys.stdin = open("input.txt")

for _ in range(10):
    n = int(input())
    li = [list(map(int, input().split())) for i in range(n)]

    # 계산의 편의성을 위해 테이블을 옆으로 돌린다. // 전치 행렬
    for i in range(n):
        for j in range(n):
            if i < j:
                li[i][j], li[j][i] = li[j][i], li[i][j]
    # 전치 행렬을 만듬으로써 행만 확인하면 된다.

    answer = 0
    for i in li:
        cnt = 0
        for j in i:
            if j == 1:
                cnt += 1
            if cnt != 0 and j == 2:
                cnt = 0
    # 이 문제의 핵심. 1이 2개고 2가 1개이면, 1이 밀고 가는게 아니라 그 자리에서 멈춘다는 것..
    # 따라서 0으로 초기화를 시켜주어야 한다.
                answer += 1

    print(f"#{_ + 1} {answer}")

# ex
# 7
# 1 0 2 0 1 0 1
# 0 2 0 0 0 0 0
# 0 0 1 0 0 1 0
# 0 0 0 0 1 2 2
# 0 0 0 0 0 1 0
# 0 0 2 1 0 2 1
# 0 0 1 2 2 0 2