# a= "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
# b = []
# for i in a:
#     b += i

# c = list(map(lambda x : ord('E') - ord(x), b))

# print(sum(c))

# 회문 재귀

#abcba
# a = input('문자열을 입력하세요: ')
# def ex(a):
#     if len(a) <= 1:
#         return True
#     elif a[0] == a[-1]:
#         return ex(a[1:-1])
#     else:
#         return False

# print(ex(a))

# 앙대 교수님의 재귀

# n = int(input('숫자: '))
# def re(n):
#     # answer_open: ('어느 한 컴퓨터 공학과 학생이 유명한 교수님을 찾아가 물었다.')
#     answer = ('"재귀함수가 뭔가요?"\n "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n 그의 답은 대부분 옳았다고 하네.\n 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#     answer_end = ("재귀함수는 자기 자신을 호출하는 함수라네")
#     answer_end2 = ('____' + '라고 답하였지')
#     if n == 0:
#         return answer
#     else:
#         return answer + re(n-1)


# print(re(n))

# a = [14, 523, 5435, 13, 1238794,12, -1, -4213]
# total = 0

# for i in a:
#     total += i

# print(total)

# user_input = ''
# while user_input != '안녕' and user_input != 'ㅎㅇ':
#     print("안녕")
#     user_input = input("말해봐 :")

# a = list(map(int, input().split()))

# b = [1, 1, 2, 2, 2, 8]


# for i in range(len(a)):
#     print(b[i] - a[i], end = ' ')

# A = int(input())
# B = int(input())

# print(A + B)
# a = input().strip()
# if not a:
#     print(0)
# else:
#     print(a.count(' ')+1)

# a = input().upper()

# max_alpha = ''
# cnt = 0
# temp = 0

# for i in a:
#     temp = a.count(i)
#     if temp > cnt:
#         max_alpha = i
#         cnt = temp
#     elif temp == cnt:
#         max_alpha = '?'
#     a = a.replace(i,'')

# print(a)
# print(max_alpha)

# a = list(map(int, input().split()))

# if a[0] > a[1]:
#     print('>')
# elif a[0] < a[1]:
#     print('<')
# else:
#     print('==')

# cnt = int(input())
# score = list(map(int, input().split()))
# total_new = 0

# max_score = max(score)

# for i in score:
#     total_new += i/max_score*100

# print(total_new/cnt)

n = int(input())

for i in range(n):
    print('*'*(i+1))