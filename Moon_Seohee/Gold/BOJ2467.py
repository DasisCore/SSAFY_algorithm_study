# BOJ2467 용액 - 투포인터
N = int(input())
li = list(map(int, input().split())) # input자체가 오름차순으로 들어옴
a = li[0]
b = li[N-1]
s = 0
e = N-1

while s < e:
    if abs(a+b) > abs(li[s] +li[e]):
        a = li[s]
        b = li[e]
    if li[s] + li[e] > 0: # 양수
        e -= 1
    elif li[s] + li[e] < 0: # 음수
        s += 1
    else :
        print(li[s], li[e])
        break
if li[s] + li[e] !=0:
    print(a, b)
