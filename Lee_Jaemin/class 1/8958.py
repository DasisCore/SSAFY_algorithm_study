T= int(input())

for tc in range(1,T+1):
    quiz=input()
    total = 0
    cnt = 1
    for i in quiz:
        if i == 'O':
            total +=cnt
            cnt+=1
        else:
            cnt=1
    print(total)