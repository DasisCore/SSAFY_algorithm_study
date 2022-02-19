# 6190. 정곤이의 단조 증가하는 수

import sys
sys.stdin = open("s_input.txt")

def check(n):  # 단조 증가하는 수인지 체크
    if n < 10:                              # 한자리 수면 무조건 단조 증가
        return True
    else:
        while n != 0:                       # 나머지와 몫을 이용하여 단조 판별
            a = n % 10
            n = n // 10
            b = n % 10
            if a < b:
                return False
        else:
            return True

T = int(input())
for _ in range(T):
    n = int(input())
    li = list(map(int, input().split()))

    danjo = []
    for i in range(n - 1):                  # 나올 수 있는 모든 조합
        for j in range(i + 1, n):
            danjo.append(li[i] * li[j])

    answer = []
    for i in danjo:
        if check(i) == True:                # 단조이면 answer에 넣는다
            answer.append(i)

    if len(answer) == 0:                    # 단조 증가인 수가 없으므로 -1 출력
        print(f"#{_ + 1} -1")
    else:                                   # 단조 증가인 수 중에서 최댓값 출력
        print(f"#{_ + 1} {max(answer)}")
