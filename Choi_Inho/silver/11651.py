import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

for i in arr:
    print(*i)