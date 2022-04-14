# 1107. 리모컨

# 문제
# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
# 수빈이가 지금 보고 있는 채널은 100번이다.
#
# 입력
# 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.
#
# 출력
# 첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

###############################################################################################


# 백트래킹 풀이 // 시간초과
import sys
sys.setrecursionlimit(1 << 30)

def recur(cur):
    global ans

    if 0 < cur <= len(str(n)) + 1:
        if ans > abs(n - int("".join(result))) + len(result):
            ans = abs(n - int("".join(result))) + len(result)
        if cur == len(str(n)) + 1:
            return

    for i in arr:
        if sum(map(int, result)) == 0 and i == 0 and cur > 0:
            continue
        result.append(str(i))
        recur(cur + 1)
        result.pop()

n = int(input())
m = int(input())
if m != 0:
    li = list(map(int, input().split()))
else:
    li = []

arr = []
for i in range(0, 10):
    if i in li:
        continue
    arr.append(i)

ans = 1 << 40
result = []
if arr:
    recur(0)
    print(min(ans, abs(n - 100)))
else:
    print(abs(n - 100))





# 완전탐색 풀이

n = int(input())
ans = abs(100 - n)
m = int(input())
if m:
    broken = list(input().split())
else:
    broken = list()

for num in range(1000001):
    for N in str(num):
        if N in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - n))
print(ans)
