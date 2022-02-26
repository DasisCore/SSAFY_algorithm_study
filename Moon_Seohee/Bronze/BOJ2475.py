# BOJ2475 검증수
lst = list(map(int, input().split()))
total = 0
for i in lst:
    i = i * i
    total += i
print(total%10)