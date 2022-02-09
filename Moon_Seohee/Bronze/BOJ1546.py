# BOJ 1546 평균
N = int(input())
subs = list(map(int, input().split()))
M = 0
for sub in subs:
    if sub > M:
        M = sub

new_subs_sum = 0
for new_sub in subs:
    new_sub = new_sub / M * 100
    new_subs_sum += new_sub

print(new_subs_sum/N)