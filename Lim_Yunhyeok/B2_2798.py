N, M = map(int, input().split())
lst = list(map(int,input().split()))    # 카드들을 리스트에 담는다.

sum = 0 # 3개를 더한 sum
result = 0  # 조건을 만족시키는 가장 큰 sum을 담을 result 값 

for i in range(N):  # 조합이니 for문을 통과하면 똑같은 걸 반복하지 않게 범위를 지정해준다.
    sum = lst[i]
    for j in range(i+1,N):
        if sum + lst[j] < M:    # 2개를 더한 순간, M보다 같거나 커지면 다시 두번째 숫자를 고른다.
            sum += lst[j]
        else: continue
        for k in range(j+1,N):
            if sum + lst[k] <= M and result < sum + lst[k]: # 3개를 더한 값이 M보다 작거나 같고 result보다 크면 result를 변경
                result = sum + lst[k]
        sum -= lst[j]   # 2번째 숫자를 변경할 때 그 전에 더해준 값을 다시 빼준다.

print(result)

# 풀이: https://velog.io/@yunhlim/Baekjoon-2798.-%EB%B8%94%EB%9E%99%EC%9E%AD-B2