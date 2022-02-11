# BOJ 10810 최소 최대

N = int(input())
nums = list(map(int, input().split()))
max_value = -1000001
min_value = 1000001


for i in nums:
    
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i
print(f"{min_value} {max_value}")