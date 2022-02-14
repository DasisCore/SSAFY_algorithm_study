# 2116. 주사위 쌓기

# 문제
# 천수는 여러 종류의 주사위를 가지고 쌓기 놀이를 하고 있다. 주사위의 모양은 모두 크기가 같은 정육면체이며 각 면에는 1부터 6까지의 숫자가 하나씩 적혀있다. 그러나 보통 주사위처럼 마주 보는 면에 적혀진 숫자의 합이 반드시 7이 되는 것은 아니다.
# 주사위 쌓기 놀이는 아래에서부터 1번 주사위, 2번 주사위, 3번 주사위, … 의 순서로 쌓는 것이다. 쌓을 때 다음과 같은 규칙을 지켜야 한다: 서로 붙어 있는 두 개의 주사위에서 아래에 있는 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 한다. 다시 말해서, 1번 주사위 윗면의 숫자는 2번 주사위 아랫면의 숫자와 같고, 2번 주사위 윗면의 숫자는 3번 주사위 아랫면의 숫자와 같아야 한다. 단, 1번 주사위는 마음대로 놓을 수 있다.
# 이렇게 쌓아 놓으면 긴 사각 기둥이 된다. 이 사각 기둥에는 4개의 긴 옆면이 있다. 이 4개의 옆면 중에서 어느 한 면의 숫자의 합이 최대가 되도록 주사위를 쌓고자 한다. 이렇게 하기 위하여 각 주사위를 위 아래를 고정한 채 옆으로 90도, 180도, 또는 270도 돌릴 수 있다. 한 옆면의 숫자의 합의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫줄에는 주사위의 개수가 입력된다. 그 다음 줄부터는 한 줄에 하나씩 주사위의 종류가 1번 주사위부터 주사위 번호 순서대로 입력된다. 주사위의 종류는 각 면에 적혀진 숫자가 그림1에 있는 주사위의 전개도에서 A, B, C, D, E, F 의 순서로 입력된다. 입력되는 숫자 사이에는 빈 칸이 하나씩 있다. 주사위의 개수는 10,000개 이하이며 종류가 같은 주사위도 있을 수 있다.
# 그림 1

# 출력
# 첫줄에 한 옆면의 숫자의 합이 가장 큰 값을 출력한다.

############################################################################################################################################################

n = int(input())
li = [list(map(int, input().split())) for i in range(n)] # 주사위들의 2차원 리스트
li += [[1, 2, 3, 4, 5, 6]] #계산엔 안쓰지만 오류가 나지 않도록 하는 허수값

high = 0
com = 0 #윗면의 수
for k in range(6): # 첫 주사위의 밑면이 될 인덱스 k
    total = 0 # 밑면이 바뀔 때 마다 최대합을 담을 변수
    i = 0 # 탐색 할 주사위 인덱스
    while i != n: # 종료 조건
        if k == 0:
            total += max(li[i][1], li[i][2], li[i][3], li[i][4])
            # 밑면과 윗면을 제외한 면들 중 최대 값을 더함
            com = li[i][5] # 윗면담기
            i += 1 # 다음 주사위
            k = li[i].index(com) # 다음 주사위의 밑면이 됨

        elif k == 5:
            total += max(li[i][1], li[i][2], li[i][3], li[i][4])
            com = li[i][0]
            i += 1
            k = li[i].index(com)

        elif k == 1:
            total += max(li[i][0], li[i][2], li[i][4], li[i][5])
            com = li[i][3]
            i += 1
            k = li[i].index(com)

        elif k == 3:
            total += max(li[i][0], li[i][2], li[i][4], li[i][5])
            com = li[i][1]
            i += 1
            k = li[i].index(com)

        elif k == 2:
            total += max(li[i][0], li[i][1], li[i][3], li[i][5])
            com = li[i][4]
            i += 1
            k = li[i].index(com)

        elif k == 4:
            total += max(li[i][0], li[i][1], li[i][3], li[i][5])
            com = li[i][2]
            i += 1
            k = li[i].index(com)


    if total > high:
        high = total

print(high)






















