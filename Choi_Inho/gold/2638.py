import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    list(map(int, input().split()))
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = [[0] * M for _ in range(N)]

print(arr)