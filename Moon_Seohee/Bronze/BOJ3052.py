# BOJ3052 나머지

from tabnanny import check


check = [0] * 42
for i in range(10):
    i = int(input()) % 42
    check[i] += 1
cnt = 0
for j in check:
    if j > 0:
        cnt += 1
print(cnt)