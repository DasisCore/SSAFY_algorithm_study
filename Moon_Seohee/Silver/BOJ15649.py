# BOJ15649 N과 M
import itertools

N, M = map(int, input().split())
nums = []
for i in range(1, N+1):
    nums.append(i)
perms = list(itertools.permutations(nums, M))
for j in perms:
    print(*j, sep=" ")