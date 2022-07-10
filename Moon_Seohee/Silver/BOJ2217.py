# BOJ2217 로프
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)

ans = 0
tem = 1
for i in lst:
    ans = max(ans, i*tem)
    tem += 1
print(ans)