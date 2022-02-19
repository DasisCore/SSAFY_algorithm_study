# 1959. 두 개의 숫자열
import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:                               # n의 리스트 길이가 더 길도록 값을 교환 함.
        n, m = m, n
        a, b = b, a

    answer = 0
    for i in range(m - n + 1):              # 한칸씩 밀면서 전부 다 계산
        total = 0
        for j in range(n):
            total += a[j] * b[j + i]        # 각 자리의 곱을 더해서 계산하는 과정

        if total > answer:                  # 최댓값을 정답으로 결정함.
            answer = total
    print(f"#{_ + 1} {answer}")


