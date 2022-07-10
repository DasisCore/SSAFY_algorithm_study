# BOJ 10825 국영수
import sys
input=sys.stdin.readline

N =int(input())
lst = []
for _ in range(N):
    i = list(map(str, input().split()))
    i[1] = int(i[1])
    i[2] = int(i[2])
    i[3] = int(i[3])
    lst.append(i)

lst.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for student in lst:
    print(student[0])