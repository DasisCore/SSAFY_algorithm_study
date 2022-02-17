# BOJ 3273 두 수의 합
def mysort(a):
    for i in range(len(a)):
        for j in range(len(a)-i):
            if a[i] > a[i+j]:
                a[i], a[i+j] = a[i+j], a[i]
    return(a)

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr = sorted(arr)
s = 0
e = n - 1
cnt = 0
while s < e:
    if arr[s] + arr[e] == x:
        cnt += 1
        s += 1
    if arr[s] + arr[e] < x:
        s += 1
    elif arr[s] + arr[e] > x:
        e -= 1
print(cnt)