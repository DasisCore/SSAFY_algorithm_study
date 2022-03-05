# BOJ1978
def find_primenumber(x):
    for i in range(2,x):
        if x % i == 0:
            return(0)
    return(1)

N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i > 1: # 1은 소수가 아니니까
        if find_primenumber(i) == 1:
            cnt += 1
print(cnt)