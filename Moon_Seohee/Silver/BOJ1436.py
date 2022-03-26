# BOJ1436 영화감독 숌
N = int(input())

a = N // 15
b = N % 15

if a == 0:
    if 0< b < 6:
        print(f"{b}666")