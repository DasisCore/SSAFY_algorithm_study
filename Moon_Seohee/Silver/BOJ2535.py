# BOJ2535 아시아 정보올림피아드
N = int(input())
arr = [] # input 리스트
for i in range(N):
    i = list(map(int, input().split()))
    arr.append(i)
arr.sort(key=lambda x:x[2], reverse=True) # 점수 기준, 내림차순 정렬

print(arr[0][0], arr[0][1], sep=" ")
print(arr[1][0], arr[1][1], sep=" ")

a = 0
while a + 2 < N:
    if arr[0][0] != arr[1][0]:
        print(arr[2 + a][0], arr[2 + a][1], sep=" ")
        break
    else: # 금과 은이 같은 나라일때
        if arr[0][0] == arr[2 + a][0]: # 동도 같은 나라
            a += 1 # 한 칸 옆으로
        else: # 다르면 출력
            print(arr[2 + a][0], arr[2 + a][1], sep=" ")
            break
