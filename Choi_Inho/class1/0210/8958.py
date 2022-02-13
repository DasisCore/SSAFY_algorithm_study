T = int(input())

for tc in range(T):
    OX = input()
    score = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            score += 1
            if i != 0:
                for j in range(i-1, -1, -1):
                    if OX[i] != OX[j]:
                        score += i - j -1
                        break
    
    print(score)