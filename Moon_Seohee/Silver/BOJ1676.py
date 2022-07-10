# BOJ 1676 팩토리얼 0의 개수
N = int(input())
five = 0
two = 0

for i in range(N, 0, -1):
    while True:
        if i % 5 == 0:
            five += 1
            i = i // 5
        else:
            break

    while True:
        if i % 2 == 0:
            two += 1
            i = i // 2
        else:
            break

if five == 0 or two == 0:
    print(0)
else:
    print(min(five, two))