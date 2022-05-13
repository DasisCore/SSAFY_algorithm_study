#BOJ11004 K번째 수
N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(lst[K-1])