# BOJ 8958번 OX퀴즈
n = int(input())

for i in range(n):
    i = input()
    sum_list = []
    tem = 0
    for j in i:
        if j == 'O':
            tem += 1
            sum_list.append(tem)
        else:
            tem = 0
    print(sum(sum_list))