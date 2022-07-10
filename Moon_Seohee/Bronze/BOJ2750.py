# BOJ2750 수 정렬하기
N = int(input())
arr = []
for i in range(N):
    i = int(input())
    arr.append(i)
arr.sort()
for j in arr:
    print(j)