# BOJ 5800 성적 통계 
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    arr.sort(reverse=True)
    ans = 0
    for i in range(len(arr)-1):
        tem = arr[i] - arr[i+1]
        ans = max(ans, tem)
    print(f"Class {tc}")
    print(f"Max {arr[0]}, Min {arr[-1]}, Largest gap {ans}")