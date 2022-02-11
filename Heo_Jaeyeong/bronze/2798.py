# 2798. 블랙잭

n, m = map(int, input().split())
li = list(map(int, input().split()))

maxnum = 0
for i in range(0, len(li)-2):
    for j in range(i + 1, len(li)-1):
        for k in range(j + 1, len(li)):
            card = li[i] + li[j] + li[k]
            if card > maxnum and card <= m:
                maxnum = card

print(maxnum)
