# 15650. N과 M(2)

# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
#
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
#
# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

########################################################################################

def recur(cur, l):
    if cur == m:
        print(*arr)
        return

    for i in range(l, n + 1):
        if visited[i] == True:
            continue

        arr[cur] = i
        visited[i] = True # 사용한 수는 다시 사용하지 않음. (중복 방지)
        recur(cur + 1, i + 1) # 첫 루프 이후에는 l의 값은 i보다 높아야 한다.
        visited[i] = False # 이후 재귀를 위한 초기화

n, m = map(int, input().split())

arr = [0 for i in range(m)]
visited = [False for _ in range(n + 1)]

recur(0, 1) # 처음 for문의 시작만 1로 시작하면 되므로 l = 1