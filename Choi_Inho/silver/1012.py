import sys

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    pass