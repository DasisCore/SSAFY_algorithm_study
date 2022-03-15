# 14889. 스타트와 링크

# 문제
# 오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.
# BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.
# N=4이고, S가 아래와 같은 경우를 살펴보자.
# i\j	1	2	3	4
# 1	 	1	2	3
# 2	4	 	5	6
# 3	7	1	 	2
# 4	3	4	5
# 예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.
# 스타트 팀: S12 + S21 = 1 + 4 = 5
# 링크 팀: S34 + S43 = 2 + 5 = 7
# 1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.
# 스타트 팀: S13 + S31 = 2 + 7 = 9
# 링크 팀: S24 + S42 = 6 + 4 = 10
# 축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.
#
# 입력
# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

################################################################################################################################

# def check(li1, li2):
#     global answer
#     start = 0
#     link = 0
#
#     for i in range(n // 2):
#         for j in range(i, n // 2):
#             start += li[li1[i] - 1][li1[j] - 1] + li[li1[j] - 1][li1[i] - 1]
#             link += li[li2[i] - 1][li2[j] - 1] + li[li2[j] - 1][li2[i] - 1]
#
#     total = abs(start - link)
#     answer = min(answer, total)
#
#
# def recur(cur):
#     global lst, n
#
#     if cur == n:
#         li1 = list(lst[: n // 2])
#         li2 = list(lst[n // 2:])
#         check(li1, li2)
#         return
#
#     for i in range(n):
#         if visited[i]:
#             continue
#
#         visited[i] = 1
#         lst.append(i + 1)
#         recur(cur + 1)
#         visited[i] = 0
#         lst.pop()
#
#
#
# n = int(input())
# li = [list(map(int, input().split())) for i in range(n)]
# lst = []
# answer = 999999999
# visited = [0] * n
# recur(0)
# print(answer)


import sys

input = sys.stdin.readline


def recur(cur, cnt):
    global answer

    # 축구 인원이 반으로 나눠졌을 때
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                # 둘다 1이면 start
                if visited[i] and visited[j]:
                    start += li[i][j]

                # 둘 다 0이면 link
                elif not visited[i] and not visited[j]:
                    link += li[i][j]
        answer = min(answer, abs(start - link))

    for i in range(cur, n):
        if visited[i]:
            continue

        visited[i] = 1
        recur(i + 1, cnt + 1)
        visited[i] = 0


n = int(input())
li = [list(map(int, input().split())) for i in range(n)]

visited = [0 for i in range(n)]
answer = sys.maxsize
recur(0, 0)
print(answer)

