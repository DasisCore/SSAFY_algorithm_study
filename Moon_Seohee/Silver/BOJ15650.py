# BOJ15650 N과 M(2)
from itertools import combinations

N, M = map(int, input().split())
nums = []
for i in range(1, N+1):
    nums.append(i)
perms = list(combinations(nums, M))
for j in perms:
    print(*j, sep=" ")
