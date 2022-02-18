#BOJ2309 일곱난쟁이 - 투포인터

arr = [] #9명의 난쟁이 키
for i in range(9):
    a = int(input())
    arr.append(a)
arr.sort() # 오름차순 정렬

s = 0 # start 배열의 가장 첫 인덱스 숫자
e = 8 # end 배열의 가장 마지막 인덱스 숫자
total = sum(arr) # 총합에서 2개를 빼서 100일때 찾기
while True:
    if (total-arr[s]-arr[e]) == 100:
        break
    elif (total-arr[s]-arr[e]) < 100: # 총합보다 작을 때
        e -= 1
    elif (total-arr[s]-arr[e]) > 100: # 총합보다 클 때
        s += 1

for i in range(9):
    if i != s and i != e: # 인덱스 숫자가 s랑 e가 아닐 때 출력
        print(arr[i])