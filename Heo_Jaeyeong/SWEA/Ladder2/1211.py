# 1211. Ladder2



import copy, sys
sys.stdin = open("input.txt")

for _ in range(10):
    n = int(input())
    li = [[0] + list(map(int, input().split())) + [0] for i in range(100)]

    start = [] # 출발점 인덱스 찾기
    for i in range(len(li[0])):
        if li[0][i] == 1:
            start.append(i)

    maxnum = 999999999
    for j in start:
        i = 0
        cnt = 0
        a = copy.deepcopy(li) # 원본 리스트가 손상되면 안되므로 deepcopy 이용
        b = j
        while i < 100:
            if a[i][j - 1] == 1: # 왼쪽 확인
                a[i][j] = 0
                j -= 1
                cnt += 1
            elif a[i][j + 1] == 1: # 오른쪽 확인
                a[i][j] = 0
                j += 1
                cnt += 1
            else:
                i += 1
                cnt += 1
        else:
            if cnt < maxnum:
                maxnum = cnt
                answer = b

    print(f"#{_ + 1} {answer - 1}") # 패딩으로 인해 -1을 해준다.
