# BOJ2470 두 용액
''' 함수 정의하면 시간초과
def mysort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i):
            if a[i] > a[i+j]:
                a[i], a[i+j] = a[i+j], a[i]
    return(a)
'''
N = int(input())
li = list(map(int, input().split()))
li.sort() # 오름차순으로 정렬해줌

s = 0 # 인덱스 시작 숫자
e = N - 1 # 인덱스 마지막 숫자
x = li[0]
y = li[N-1]

if li[0] > 0:
    print(li[0], li[1])
    
elif li[-1] < 0:
    print(li[-2], li[-1])
    
else :
    while s < e:
        if abs(x+y) > abs(li[s]+li[e]):
            x = li[s]
            y = li[e]

        if li[s] + li[e] < 0: # 음수
            s += 1 # 작은 수의 값을 증가해주기
        elif li[s] + li[e] > 0: # 양수
            e -= 1 # 큰 수의 값을 감소시켜주기
        else: # 절댓값 합이 0이면 최소값이므로 바로 출력
            print(li[s], li[e])
            break # 반복문 종료
    if li[s] + li[e] != 0: # 0일때는 위에서 이미 출력해줘서
        print(x, y)