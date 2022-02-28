# BOJ10733 제로
K = int(input())
stack = []
for i in range(K):
    a = int(input())
    if a != 0:
        stack.append(a)
    else:
        stack.pop()
if stack == []:
    print(0)
else:
    total = 0
    for j in stack:
        total += j
    print(total)