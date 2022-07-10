# BOJ2667 단지번호붙이기
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 1
cntlst = []

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(N):
    for j in range(N):
        tem = 0 
        if arr[i][j] == 1:
            tem += 1
            cnt += 1
            arr[i][j] = 0
            for a in range(1, N+1): # 인덱스 범위 안에서
                for b in range(1, N+1): # 인덱스 범위 안에서
                    ni = i + 
