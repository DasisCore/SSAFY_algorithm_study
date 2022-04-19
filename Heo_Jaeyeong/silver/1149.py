# 1149. RGB거리

# 문제
# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
#
# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

####################################################################################################################################

import sys
sys.setrecursionlimit(1 << 30)

def recur(cur, prv):
    if cur == n:
        return 0

    # 방문한 적이 있다면 dp[cur][prv]를 리턴한다.
    if dp[cur][prv] != 100000:
        return dp[cur][prv]

    for i in range(0, 3):
        # 문제의 조건
        if cur > 0 and prv == i:
            continue
        # 여태까지 온 쌓아둔 dp와 현재 값 중 작은 것을 넣어준다.
        dp[cur][prv] = min(dp[cur][prv], recur(cur + 1, i) + li[cur][i])

    return dp[cur][prv]


n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
dp = [[100000] * (n + 1) for i in range(n + 1)]
print(recur(0, 0))