# 5431. 민석이의 과제 체크하기

import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for _ in range(T):

    n, k = map(int, input().split())

    li = [0] * (n + 1)                      # 전부 다 숙제를 안했다고 일단 가정

    no = list(map(int, input().split()))    # 숙제를 낸 사람은 1로 체크
    for i in no:
        li[i] = 1

    print(f"#{_ + 1}", end=" ")             # 출력 형식을 맞추기 위해

    for j in range(1, n+1):                 # 리스트를 순회하며 숙제를 안한 사람 출력
        if li[j] == 0:
            print(j, end=" ")
    print()                                 # 출력 형식을 맞추기 위해


