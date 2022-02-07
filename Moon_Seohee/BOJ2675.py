# BOJ 2675 문자열 반복
t = int(input())
for i in range(t):
    i = input()
    r, s = map(str, i.split())
    r = int(r)
    for j in s:
        print(j*r, end="")
    print() #다음 줄로 넘어가서 다시 input
    