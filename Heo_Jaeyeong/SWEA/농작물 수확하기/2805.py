# 2805. 농작물 수확하기

import sys
sys.stdin = open("input.txt")


T = int(input())
for _ in range(T):
    n = int(input())

    # 만약 5x5 배열이라면 마름모 형태를 만들기 위해
    # 중앙을 기준으로 양 옆으로 [0, 1, 2, 1, 0] 을 더하고 빼는 방식으로 풀었다.
    if n == 1:
        li = [0]
    else:
        li = []
        a = 0
        flag = False
        while a >= 0:
            if flag == False:
                li.append(a)
                a += 1
            elif flag == True:
                a -= 1
                li.append(a)

            if a == n // 2:
                li.append(a)
                flag = True
                # 플래그가 True가 되면 정점에서 다시 빼기 시작함.
        li = li[:n] # 초기값 때문에 -1이 리스트에 더해지므로 마지막값은 빼준다.

    farm = [] #입력값이 붙어 들어와서 일일이 떼주었다.
    for i in range(n):
        field = input()
        temp = []
        for j in field:
            temp.append(int(j))
        farm.append(temp)


    answer = 0
    mid = n // 2 #중앙을 기준점으로 잡고.
    for i in range(n): # li의 각 값만큼 빼고 더한 범위를 합산해서 answer에 더해주었다.
        area = sum(farm[i][mid - li[i]:mid + li[i] + 1])
        answer += area
    print(f"#{_ + 1} {answer}")


