# BOJ7785 회사에 있는 사람
import sys
input=sys.stdin.readline

n = int(input())
ans = set()

for i in range(n):
    people, now = input().split()
    if now == "enter":
        ans.add(people)
    elif now == "leave":
        ans.remove(people)

ans = list(ans)
ans.sort(reverse=True)
print(*ans, sep="\n")
