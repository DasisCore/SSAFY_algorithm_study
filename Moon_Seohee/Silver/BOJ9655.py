# BOJ9655 돌 게임
N = int(input())
a = N // 3
b = N % 3
if (a+b) % 2 == 0:
    print("CY")
else:
    print("SK")