# 2001. 파리퇴치
import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    li = [list(map(int, input().split())) for i in range(n)]

    maxfly = 0
    for o in range(n - m + 1):
        for k in range(n - m + 1):
            total = 0
            for i in range(m):
                for j in range(m):
                    total += li[o + i][k + j]
            if total > maxfly:
                maxfly = total

    print(f"#{_ + 1} {maxfly}")
