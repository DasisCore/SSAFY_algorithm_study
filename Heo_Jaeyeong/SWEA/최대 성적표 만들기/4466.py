# 4455. 최대 성적표 만들기

import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for _ in range(T):

    n, k = map(int, input().split())
    li = list(map(int, input().split()))

    for i in range(n): # 거품 정렬
        for j in range(n - 1):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


    total = 0
    for i in range(k):
        total += li[i]
    print(f"#{_ + 1} {total}")


