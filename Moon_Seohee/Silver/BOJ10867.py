# BOJ10867 중복 빼고 정렬하기
N = int(input())
lst = list(map(int, input().split( )))
lst = set(lst)
lst= list(lst)
lst.sort()
print(*lst, sep=" ")