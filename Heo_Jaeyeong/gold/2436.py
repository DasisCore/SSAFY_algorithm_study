# 2436. 공약수
# 문제
# 어떤 두 자연수에 공통인 약수들 중에서 가장 큰 수를 최대공약수라고 하고, 두 자연수의 공통인 배수들 중에서 가장 작은 수를 최소공배수라고 한다. 
# 예를 들어, 두 자연수 12와 90의 최대공약수는 6이며, 최소공배수는 180이다.
# 이와 반대로 두 개의 자연수 A, B가 주어졌을 때, A를 최대공약수로, B를 최소공배수로 하는 두 개의 자연수를 구할 수 있다. 그러나, 이러한 두 개의 자연수 쌍은 여러 개 있을 수 있으며, 또한 없을 수도 있다. 
# 예를 들어, 최대공약수가 6이며 최소공배수가 180인 두 정수는 위의 예에서와 같이 12와 90일 수도 있으며, 30과 36, 18과 60, 혹은 6과 180일 수도 있다. 그러나, 최대공약수가 6이며 최소공배수가 20인 두 자연수는 있을 수 없다.
# 두 개의 자연수가 주어졌을 때, 이 두 수를 최대공약수와 최소공배수로 하는 두 개의 자연수를 구하는 프로그램을 작성하시오. 

# 입력
# 첫째 줄에 두 개의 자연수가 빈칸을 사이에 두고 주어진다. 첫 번째 수는 어떤 두 개의 자연수의 최대공약수이고, 두 번째 수는 그 자연수들의 최소공배수이다. 입력되는 두 자연수는 2 이상 100,000,000 이하이다.

# 출력
# 첫째 줄에는 입력되는 두 자연수를 최대공약수와 최소공배수로 하는 두 개의 자연수를 크기가 작은 수부터 하나의 공백을 사이에 두고 출력한다. 입력되는 두 자연수를 최대공약수와 최소공배수로 하는 두 개의 자연수 쌍이 여러 개 있는 경우에는 두 자연수의 합이 최소가 되는 두 수를 출력한다.
################################################################################################

## 두 수의 최대공약수 구하기
def prime(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

a, b = map(int, input().split())
N = b // a 
# 최소공배수 최대공약수의 성질


li = [] # N의 약수 구하기
for i in range(1, N + 1):
    if i * i > N:
        break
    if N % i == 0:
        li.append(i)
        if i * i != N:
            li.append(N // i)
li.sort() #N의 약수 정렬

srs = 999999999999

# 투포인터 사용
s = 0
e = len(li) - 1

# 두 수가 서로소이면서 곱했을 때 N인 경우
while s < e:
    if li[s] * li[e] == N and prime(li[s], li[e]) == 1:
        if li[s] + li[e] < srs: # 최소값만 저장
            srs = li[s] + li[e]
            x = li[s]
            y = li[e]
        s += 1
        continue
    elif li[s] * li[e] > N:
        e -= 1
    else:
        s += 1

if a == b: # a, b가 같은 경우 예외 // 1 1
    print(a, a)
else:
    print(a * x, a * y)
