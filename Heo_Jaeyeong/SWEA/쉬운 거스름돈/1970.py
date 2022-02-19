# 1970. 쉬운 거스름돈

import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):

    # 사용되는 화폐의 종류
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    m = int(input()) # 입력되는 돈

    li = [] # 종류당 개수가 담길 리스트
    for i in money:
        li.append(m // i) # 종류당 돈의 개수
        m = m % i  # 남은 거스름돈

    print(f"#{_ + 1}")
    print(*li)
