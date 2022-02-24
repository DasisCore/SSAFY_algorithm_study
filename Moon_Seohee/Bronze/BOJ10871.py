# BOJ10871 X보다 작은 수

N, X = map(int, input().split())
arr = list(map(int, input().split()))
result = []
for i in arr:
    if i < X:
        result.append(i)

for j in result:
    print(j, end=" ")