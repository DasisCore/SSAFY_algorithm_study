# BOJ 2908 상수
a, b = map(str, input().split())
a2 = int(a[::-1])
b2 = int(b[::-1])

if a2 > b2:
    print(a2)
else:
    print(b2)